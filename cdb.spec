%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Constant DataBase
Name:		cdb
Version:	0.75
Release:	2
License:	Public Domain
Group:		Databases
Url:		https://cr.yp.to/cdb.html
Source0:	%{name}-%{version}.tar.gz
Patch0:		cdb-0.75-errno.patch
Patch1:		cdb-0.75-stdint.patch
Obsoletes:	cdb-devel < 0.75

%description
cdb is a fast, reliable, lightweight package for creating and reading
constant databases.

%files
%doc README TODO
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
sed -i -e 's/head -1/head -n 1/g' Makefile

%build
echo "gcc %{optflags}">conf-cc
echo "gcc %{ldflags}">>conf-ld
make

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -m 755 cdbdump %{buildroot}%{_bindir}/
install -m 755 cdbget %{buildroot}%{_bindir}/
install -m 755 cdbmake %{buildroot}%{_bindir}/
install -m 755 cdbmake-12 %{buildroot}%{_bindir}/
install -m 755 cdbmake-sv %{buildroot}%{_bindir}/
install -m 755 cdbstats %{buildroot}%{_bindir}/
install -m 755 cdbtest %{buildroot}%{_bindir}/

