Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(pl):	GnuPG - GNU Privacy Guard - narz�dzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(es):	Criptograf�a con llaves p�blicas (asim�tricas). GPL
Summary(ja):	�����奢�ʥ��ߥ�˥��������ȥǡ�����¸�Τ���� GNU �桼�ƥ���ƥ���
Summary(pt_BR):	Criptografia com chaves p�blicas (assim�tricas). GPL
Summary(ru):	GNU Privacy Guard - ��������� ������ PGP
Summary(uk):	GNU Privacy Guard - צ���� ��ͦ�� PGP
Name:		gnupg
Version:	1.0.7
Release:	2
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	libcap-devel
BuildRequires:	openldap-devel 
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%description -l es
GnuPG es un sustituto completo y de libre distribuci�n para PGP. Como
no utiliza IDEA y RSA, su uso no est� restringido. Est� casi
completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l ja
GnuPG (GNU Privacy Guard)
�ϥǡ����ΰŹ沽�ȥǥ��������̾�κ����Τ���� GNU
�桼�ƥ���ƥ��Ǥ���GnuPG �Ϲ��٤ʸ�����ǽ�Ϥ������ RFC2440
�ǵ��Ҥ���Ƥ��� OpenPGP ���󥿡��ͥå�ɸ�����Ƥ�Ŭ�礷�Ƥ��ޤ���
GnuPG ���õ����르�ꥺ��ϻ��Ѥ��Ƥ��ʤ��Τǡ�PGP2
�Τ��������������� �ȸߴ���������ޤ���(PGP2.x ��
����Ū���õ��Ǥ��� IDEA �ȡ� 2000ǯ 9��20���ޤ� USA �Ǥ��õ��Ǥ��� RSA
�Τߤ��Ѥ��Ƥ��ޤ�)

%description -l pl
GnuPG jest narz�dziem do bezpiecznej komunikacji i bezpiecznego
przechowywania danych. Mo�e by� u�ywany do szyfrowania oraz
podpisywania danych. Umo�liwia zaawansowane zarz�dzanie kluczami i
spe�nia normy zdefiniowane w standardzie OpenPGP, kt�ry jest opisany w
RFC2440.

%description -l pt_BR
O GnuPG � um substituto completo e de livre distribui��o para o PGP.
Como ele n�o usa IDEA e RSA seu uso � irrestrito. Est� quase
completamente de acordo com o rascunho (draft) OpenPGP.

%description -l ru
GnuPG �������� ������ � ��������� ������� ��� PGP. ��� ��� �� ��
���������� �� IDEA, �� RSA, �� �� ��� ������������� �� �������������
������� �����������. GnuPG ������������� ������������ OpenPGP
(RFC2440).

%description -l uk
GnuPG � ������ �� צ����� ��ͦ��� PGP. ��� �� ����������դ Φ IDEA,
�Φ RSA, ��� �� �� ���� ������������ �� ������������ Φ���� ��������.
GnuPG צ���צ��� �����Ʀ��æ� OpenPGP (RFC2440).

%prep
%setup -q

%build
%configure \
	--with-capabilities \
	--enable-ldap \
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*

%{_mandir}/man?/*
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel
