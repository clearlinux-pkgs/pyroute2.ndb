#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2.ndb
Version  : 0.6.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/68/ac/fc35b5d62ac6c3245a5c414485b65498c8544b996154bac8d1e44ce8e0f9/pyroute2.ndb-0.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/ac/fc35b5d62ac6c3245a5c414485b65498c8544b996154bac8d1e44ce8e0f9/pyroute2.ndb-0.6.4.tar.gz
Summary  : Python Netlink library: NDB module
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pyroute2.ndb-bin = %{version}-%{release}
Requires: pyroute2.ndb-license = %{version}-%{release}
Requires: pyroute2.ndb-python = %{version}-%{release}
Requires: pyroute2.ndb-python3 = %{version}-%{release}
Requires: pyroute2.core
BuildRequires : buildreq-distutils3
BuildRequires : pyroute2.core

%description
============
        
        PyRoute2 is a pure Python **netlink** library.
        
        NDB is a high-level network management module. It provides a transactional DB
        with multiple sources, from local RTNL source to netns and remote systems. The
        DB provides Python API and HTTP RPC (json and plain text), my run as a
        standalone service or may be used as a Python module.
        
        links
        =====

%package bin
Summary: bin components for the pyroute2.ndb package.
Group: Binaries
Requires: pyroute2.ndb-license = %{version}-%{release}

%description bin
bin components for the pyroute2.ndb package.


%package license
Summary: license components for the pyroute2.ndb package.
Group: Default

%description license
license components for the pyroute2.ndb package.


%package python
Summary: python components for the pyroute2.ndb package.
Group: Default
Requires: pyroute2.ndb-python3 = %{version}-%{release}

%description python
python components for the pyroute2.ndb package.


%package python3
Summary: python3 components for the pyroute2.ndb package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.ndb)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pyroute2.ndb package.


%prep
%setup -q -n pyroute2.ndb-0.6.4
cd %{_builddir}/pyroute2.ndb-0.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623080471
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyroute2.ndb
cp %{_builddir}/pyroute2.ndb-0.6.4/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ndb/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ndb-0.6.4/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ndb/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyroute2-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyroute2.ndb/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pyroute2.ndb/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
