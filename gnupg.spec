Summary:	gpg - GNU Privacy Guard
Summary(pl):	gpg Stra�nik Prywatno�ci GNU
Summary(ja):	�����奢�ʥ��ߥ�˥��������ȥǡ�����¸�Τ���� GNU �桼�ƥ���ƥ���
Summary(pt_BR):	Criptografia com chaves p�blicas (assim�tricas). GPL
Summary(es):	Criptograf�a con llaves p�blicas (asim�tricas). GPL
Name:		gnupg
Version:	1.0.6
Release:	3
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Patch0:		%{name}-locale.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-1.0.5-es_ES-fix.patch
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
#BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
#BuildRequires:	libtool
#BuildRequires:	automake
#BuildRequires:	autoconf
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPG is the main program for the GNUPG system. gpgm is a maintenance
tool which has some commands gpgm does not have; it is there because
it does not handle sensitive data and therefore has no need to
allocate secure memory.

%description -l pl
GPG jest g��wnym programem nale��cym do systemu GNUPG (GNU Privacy
Guard, odpowiednik programu Pretty Good Privacy na licencji GNU).

%description -l ja
GnuPG (GNU Privacy Guard) �ϥǡ����ΰŹ沽�ȥǥ��������̾�κ����Τ����
GNU �桼�ƥ���ƥ��Ǥ���GnuPG �Ϲ��٤ʸ�����ǽ�Ϥ������
RFC2440 �ǵ��Ҥ���Ƥ��� OpenPGP ���󥿡��ͥå�ɸ�����Ƥ�Ŭ�礷�Ƥ��ޤ���
GnuPG ���õ����르�ꥺ��ϻ��Ѥ��Ƥ��ʤ��Τǡ�PGP2 �Τ���������������
�ȸߴ���������ޤ���(PGP2.x �� ����Ū���õ��Ǥ��� IDEA �ȡ�
2000ǯ 9��20���ޤ� USA �Ǥ��õ��Ǥ��� RSA �Τߤ��Ѥ��Ƥ��ޤ�)

%description -l pt_BR
O GNUPG � um substituto completo e de livre distribui��o para o PGP. Como ele
n�o usa IDEA e RSA seu uso � irrestrito. Est� quase completamente de acordo com
o rascunho (draft) OpenPGP.

%description -l es
GNUPG es un sustituto completo y de libre distribuci�n para PGP. Como no
utiliza IDEA y RSA, su uso no est� restringido. Est� casi completamente de
acuerdo con el borrador (draft) OpenPGP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#rm scripts/missing
#gettextize --force --copy
#aclocal 
#autoconf
#automake -a -c --no-force
%configure2_13 \
	--with-capabilities \
%ifarch sparc sparc64
	--disable-m-guard \
%else
	--enable-m-guard \
%endif
	--without-included-gettext \
	--disable-m-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO \
	  doc/{DETAILS,FAQ,OpenPGP}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*
%{_datadir}/gnupg
