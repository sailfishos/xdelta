Summary: Delta compression tool
Name: xdelta3
Version: 0
Release: 1
License: Apache-2.0
URL: https://github.com/sailfishos/xdelta
Source0: %{name}-%{version}.tar.gz
BuildRequires: cmake

%description
This package provides the xdelta3 command-line tool for VCDIFF differential
compression, a.k.a.  delta compression.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
cmake . \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
    -DCMAKE_BUILD_TYPE=Release \
    -DXD3_BUILD_LIB=OFF \
    -DXD3_ARMOR=OFF
%make_build

%install
%make_install

%check
ctest

%files
%defattr(-,root,root)
%{_bindir}/xdelta3
%exclude %{_includedir}/xdelta3.h
%exclude %{_mandir}/man1/xdelta3.1.gz
