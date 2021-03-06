Name:           bakefile
Version:        0.2.10
Release:        5%{?dist}
Summary:        A cross-platform, cross-compiler native makefiles generator
License:        MIT
URL:            http://www.bakefile.org/
Source:         https://github.com/vslavik/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         bakefile-028-fix-import.patch

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  python-libxml2
%else
BuildRequires:  libxml2-python
%endif
BuildRequires:  python2-devel swig
Requires:       automake python2-empy

%description
Bakefile is cross-platform, cross-compiler native makefiles generator. It takes
compiler-independent description of build tasks as input and generates native
makefile (autoconf's Makefile.in, Visual C++ project, bcc makefile etc.)

%prep
%setup -q
%patch0 -p0

%build
pushd src
swig -python bkl_c.i
popd
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS NEWS README THANKS
%{_bindir}/bakefil*
%{_datadir}/bakefile
%{_mandir}/man1/bakefil*
%{_libdir}/bakefile*
%exclude %{_libdir}/%{name}/empy
%exclude %{_libdir}/%{name}/py25modules
%exclude %{_libdir}/%{name}/_bkl_c.la
%{_datadir}/aclocal/*.m4

%changelog
* Sun Sep 03 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.10-5
- Require libxml2-python for building on RHEL7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Scott Talbert <swt@techie.net> - 0.2.10-3
- Modernize packaging

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Scott Talbert <swt@techie.net> - 0.2.10-1
- Updated to 0.2.10 upstream release

* Fri Feb 17 2017 Scott Talbert <swt@techie.net> - 0.2.9-10
- Fix segfault issue by patching swig interface file (#1419786)
- Apply patch from upstream for fixing RTTI support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.9-4
- Fix FTBFS -Werror=format-security rhbz #1036997 (thanks to Dhiru Kholia)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.9-1
- Updated to 0.2.9 upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.8-5
- fix for rhbz#633520 and rhbz#652887 (thanks to Jonathan Wakely and Josef Šimánek)

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.8-4
- recompiling .py files against Python 2.7 (rhbz#623276)

* Tue Mar 02 2010 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.8-3
- Fixed Source url
- Updated BuildRequires and Requires info
- Empy python module packaged independently
- Removed files of uuid and subprocess python modules
- Removed .la files

* Tue Dec 22 2009 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.8-2
- Replaced summary information
- Updated BuildRequires and Requires information
- Replaced "{_mandir}/man1/bakefil*.gz" to "{_mandir}/man1/bakefil*"
- Correct URL and source URL
- Replaced "%%{_libdir}/*" to "%%{_libdir}/bakefile*"
- Removed useless line: "%%doc"

* Mon Dec 21 2009 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.8-1
- Initial RPM release
