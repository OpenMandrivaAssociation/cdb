Summary:	Constant DataBase
Name:		cdb
Version:	0.55
Release:	%mkrel 16
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
