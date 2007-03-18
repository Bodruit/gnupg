#
# Conditional builds:
%bcond_without	ldap	# without LDAP plugin
#
Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(cs):	GNU n�stroj pro �ifrovanou komunikaci a bezpe�n� ukl�d�n� dat
Summary(es):	Criptograf�a con llaves p�blicas (asim�tricas). GPL
Summary(ja):	�����奢�ʥ��ߥ�˥��������ȥǡ�����¸�Τ���� GNU �桼�ƥ���ƥ���
Summary(pl):	GnuPG - narz�dzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(pt_BR):	Criptografia com chaves p�blicas (assim�tricas). GPL
Summary(ru):	GNU Privacy Guard - ��������� ������ PGP
Summary(uk):	GNU Privacy Guard - צ���� ��ͦ�� PGP
Summary(zh_CN):	GPL��PGP���ܳ���
Name:		gnupg
Version:	1.4.7
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/GnuPG/gnupg/%{name}-%{version}.tar.bz2
# Source0-md5:	b06a141cca5cd1a55bbdd25ab833303c
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-fix.patch
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
BuildRequires:	libusb-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%description -l cs
GnuPG je GNU n�stroj pro bezpe�nou komunikaci a ukl�d�n� dat. M��e b�t
pou�it na �ifrov�n� dat a vytv��en� digit�ln�ch podpis�. Obsahuje
funkce pro pokro�ilou spr�vu kl��� a vyhovuje navrhovan�mu OpenPGP
Internet standardu podle RFC2440. Byl vytvo�en jako kompletn� n�hrada
za PGP. Proto�e neobsahuje �ifrovac� algoritmy IDEA nebo RSA, m��e b�t
pou��v�n bez omezen�. Proto�e GnuPG nepou��v� ��dn� patentovan�
algoritmus, nem��e b�t �pln� kompatibiln� s PGP verze 2. PGP 2.x
pou��v� algoritmy IDEA (patentov�no celosv�tov�) a RSA (patentov�no ve
Spojen�ch st�tech do 20. z��� 2000). Tyto algoritmy lze zav�st do
GnuPG pomoc� extern�ch modul�.

%description -l es
GnuPG es un sustituto completo y de libre distribuci�n para PGP. Como
no utiliza IDEA y RSA, su uso no est� restringido. Est� casi
completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l fr
GnuPG est un utilitaire GNU destin� � chiffrer des donn�es et � cr�er
des signatures �lectroniques. Il a des capacit�s avanc�es de gestion
de cl�s et il est conforme � la norme propos�e OpenPGP d�crite dans la
RFC2440. Comme GnuPG n'utilise pas d'algorithme brevet�, il n'est
compatible avec aucune version de PGP2 (PGP2.x ne sait utiliser que
l'IDEA brevet� dans le monde entier et RSA, brevet� aux �tats-Unis
jusqu'au 20 septembre 2000).

%description -l it
GnuPG (GNU Privacy Guard) � una utility GNU per la cifratura di dati e
la creazione di firme digitali. Possiede una gestione avanzata delle
chiavi ed � conforme allo standard Internet OpenPGP, descritto nella
RFC 2440. Non utilizzando algoritmi brevettati, non � compatibile con
PGP2 (PGP2.x usa solo IDEA, coperto da brevetto mondiale, ed RSA,
brevettato negli USA con scadenza 20/09/2000). Questi algoritmi sono
utilizzabili da GnuPG tramite moduli esterni.

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
GnuPG (GNU Privacy Guard) jest narz�dziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Mo�e by� u�ywany do szyfrowania
oraz podpisywania danych. Umo�liwia zaawansowane zarz�dzanie kluczami
i spe�nia normy zdefiniowane w standardzie OpenPGP, kt�ry jest opisany
w RFC2440.

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

%package plugin-keys_curl
Summary:	GnuPG plugin for allow talk to a HTTP/FTP keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy HTTP/FTP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gnupg-plugin-keys_http

%description plugin-keys_curl
GnuPG plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%description plugin-keys_curl -l pl
Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy
HTTP(S)/FTP(S).

%package plugin-keys_finger
Summary:	GnuPG plugin for allow talk to a FINGER keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy FINGER
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_finger
GnuPG plugin for allow talk to a FINGER keyserver.

%description plugin-keys_finger -l pl
Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy FINGER.

%package plugin-keys_hkp
Summary:	GnuPG plugin for allow talk to a HKP keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy HKP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_hkp
GnuPG plugin for allow talk to a HKP keyserver.

%description plugin-keys_hkp -l pl
Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy HKP.

%package plugin-keys_ldap
Summary:	GnuPG plugin for allow talk to a LDAP keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy LDAP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_ldap
GnuPG plugin for allow talk to a LDAP keyserver.

%description plugin-keys_ldap -l pl
Wtyczka GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy LDAP.

%package plugin-keys_mailto
Summary:	GnuPG plugin for allow talk to a email keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj�ca komunikowa� si� z e-mailowym serwerem kluczy
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_mailto
GnuPG plugin for allow talk to a email keyserver.

%description plugin-keys_mailto -l pl
Wtyczka GnuPG pozwalaj�ca komunikowa� si� z e-mailowym serwerem
kluczy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.sub scripts
%configure \
	--with-capabilities \
	%{?with_ldap:--enable-ldap} \
	%{!?with_ldap:--disable-ldap} \
	--disable-m-debug \
	--disable-m-guard \
	--enable-mailto \
	--without-included-gettext \
	--with-mailprog=/usr/sbin/sendmail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT{%{_datadir}/gnupg/{FAQ,faq.html},%{_infodir}/dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}/gnupg
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel
%{_mandir}/man?/*
%{_infodir}/*.info*

%files plugin-keys_finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_finger

%files plugin-keys_hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_hkp

%files plugin-keys_curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_curl

%if %{with ldap}
%files plugin-keys_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_ldap
%endif

%files plugin-keys_mailto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_mailto
