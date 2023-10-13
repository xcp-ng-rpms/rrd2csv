%global package_speccommit 35dad1a75777581e1f73de4e2005d8fb71275cd3
%global package_srccommit v1.2.6
Name:           rrd2csv
Version: 1.2.6
Release: 8%{?xsrel}%{?dist}
Summary:        Tool for converting Xen API RRDs to CSV
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          System/Hypervisor
URL:            https://github.com/xenserver/rrd2csv/
Source0: rrd2csv-1.2.6.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  xs-opam-repo
BuildRequires:  xapi-client-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel

%description
This package contains the rrd2csv tool, useful to expose live RRDD metrics on
standard output, in the CSV format.

%prep
%autosetup -p1

%build
mkdir -p %{buildroot}
DESTDIR=%{buildroot} %{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} %{__make} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/xensource/bin/rrd2csv
/opt/xensource/man/man1/rrd2csv.1

%changelog
* Mon Oct 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.2.6-8
- Bump release and rebuild

* Thu Jul 20 2023 Rob Hoes <rob.hoes@citrix.com> - 1.2.6-7
- Bump release and rebuild

* Mon Jun 19 2023 Christian Lindig <christian.lindig@citrix.com> - 1.2.6-6
- Bump release and rebuild

* Thu Jun 08 2023 Christian Lindig <christian.lindig@citrix.com> - 1.2.6-5
- Bump release and rebuild

* Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.2.6-4
- Bump release and rebuild

* Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.2.6-3
- Bump release and rebuild

* Tue Feb 28 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.2.6-2
- Change license to match the one in the source repo

* Mon Feb 20 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.2.6-1
- Same as 1.2.5, koji tooling needed an annotated tag to build

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.2.5-7
- Bump package after xs-opam update

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.2.5-6
- Bump packages after ocaml-xen-api-libs-transitional update

* Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.2.5-5
- bump packages after xs-opam update

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.2.5-3
- bump packages after xs-opam update

* Mon May 20 2019 Christian Lindig <christian.lindig@citrix.com> - 1.2.5-1
- Fix installed manpage path

* Mon May 20 2019 Christian Lindig <christian.lindig@citrix.com> - 1.1.5-2
- Fix extension of manual path after change in source Makefile

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.1.5-1
- Moved from jbuilder to dune and deprecated xcp in favour of xapi-idl.

* Tue Jan 09 2018 Marcello Seri <marcello.seri@citrix.com> - 1.0.5-1
- Add missing dependencies

* Fri Dec 08 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.4-1
- Port to jbuilder

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.2-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Dec 15 2016 Rob Hoes <rob.hoes@citrix.com> - 1.0.2-1
- git: Add metadata to the result of `git archive`

* Tue Aug 16 2016 Christian Lindig <christian.lindig@citrix.com> - 1.0.1-1
- Bump version to track new upstream release

* Tue Apr 26 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 11 2014 John Else <john.else@citrix.com> - 0.1.0-1
- Initial package for planex
