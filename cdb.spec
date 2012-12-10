Summary:	Constant DataBase
Name:		cdb
Version:	0.55
Release:	%mkrel 18
License:	Public Domain
Group:		Databases
URL:		http://cr.yp.to/cdb.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-errno.patch
BuildRequires:	man groff groff-for-man
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
cdb is a fast, reliable, lightweight package for
creating and reading constant databases.

%package devel
Summary: Static libraries and headers for cdb-%{version}
Group: Development/Databases

%description devel
Libraries and header files needed to develop
applications using cdb databases

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
echo "CC='gcc $RPM_OPT_FLAGS'">conf-cc.sh
echo "LD='gcc $RPM_OPT_FLAGS -s'">>conf-cc.sh
make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_mandir}/man{1,3}
install -m 755 12tocdbm %{buildroot}%{_bindir}/
install -m 755 cdbdump %{buildroot}%{_bindir}/
install -m 755 cdbget %{buildroot}%{_bindir}/
install -m 755 cdbmake %{buildroot}%{_bindir}/
install -m 755 cdbstats %{buildroot}%{_bindir}/
install -m 755 cdbtest %{buildroot}%{_bindir}/
install -m 644 *.1 %{buildroot}%{_mandir}/man1/
install -m 644 *.3 %{buildroot}%{_mandir}/man3/
install -m 644 libcdb.a %{buildroot}%{_libdir}/
install -m 644 libcdbmake.a %{buildroot}%{_libdir}/
install -m 644 cdb.h %{buildroot}%{_includedir}/
install -m 644 cdbmake.h %{buildroot}%{_includedir}/
install -m 644 uint32.h %{buildroot}%{_includedir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post devel
ldconfig || /bin/true

%postun devel
ldconfig || /bin/true

%files
%defattr(-,root,root)
%doc BLURB CDB CHANGES INSTALL README TODO SYSDEPS
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man3/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.55-18mdv2011.0
+ Revision: 616959
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.55-17mdv2010.0
+ Revision: 424751
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.55-16mdv2009.0
+ Revision: 243444
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.55-14mdv2008.1
+ Revision: 136288
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.55-14mdv2008.0
+ Revision: 66658
- Import cdb



* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.55-14mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 0.55-13mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.55-12mdk
- build release

* Fri Apr 25 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-11mdk
- fix buildrequires, thanks to Stefan van der Eijks robot

* Wed Mar 26 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-10mdk
- fix build on latest glibc-2.3.1

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-9mdk
- build release

* Sun Aug  4 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-8mdk
- rebuilt with gcc-3.2

* Mon May 20 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-7mdk
- rebuilt with gcc3.1

* Mon Nov 26 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-6mdk
- really use rpmlint this time :)

* Mon Nov 26 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-5mdk
- initial contrib

* Sat Feb 17 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.55-4mdk
- mandrakified original package by Bruce Guenter <bruceg@em.ca>

* Sat Oct 09 1999 Oden Eriksson <oden@kvikkjokk.com>
- Added cpu optimization

* Sun Feb 15 1998 Bruce Guenter <bruce.guenter@qcc.sk.ca>
 - as per the README file, the copyright is really public-domain

* Thu Oct 10 1997 Bruce Guenter <bruce.guenter@qcc.sk.ca>
 - added libcdbmake.a, cdbmake.h, and uint32.h to devel package
