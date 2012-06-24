Summary:     gpg - GNU Privacy Guard
Name:        gnupg
Version:     0.4.5
Release:     1
Source:      ftp://ftp.guug.de/pub/gcrypt/%{name}-%{version}.tar.gz
URL:         http://www.d.shuttle.de/isil/crypt/gnupg.html
Icon:        keyhole.gif
Copyright:   GPL
Provides:    pgp
Group:       Utilities/File
BuildRoot:   /tmp/%{name}-%{version}-root

%description
gpg is the main program for the GNUPG system. gpgm is a maintenance tool
which has some commands gpgm does not have; it is there because it does not
handle sensitive data ans therefore has no need to allocate secure memory.

%prep
%setup -q

%build
LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--disable-m-debug \
	--disable-m-guard
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

#strip $RPM_BUILD_ROOT/usr/bin/*

rm -f $RPM_BUILD_ROOT/usr/man/man1/gpgm.1
echo ".so gpg.1" >$RPM_BUILD_ROOT/usr/man/man1/gpgm.1
gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
%attr(755, root, root) /usr/lib/gnupg
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnupg.mo
%lang(es) /usr/share/locale/es*/LC_MESSAGES/gnupg.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnupg.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnupg.mo
%lang(pt) /usr/share/locale/pt*/LC_MESSAGES/gnupg.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/gnupg.mo

%changelog
* Sat Dec 12 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.5-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- s/rfcs/OpenPGP/ in %doc,
- added pt* and ru .mo files.

* Mon Sep 21 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.0-1]
- first release in rpm package.
