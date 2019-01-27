Name: date
Version: 2.4.1
Release: 1%{?dist}
Summary: A date and time library based on the C++11/14/17 <chrono> header  

License: MIT 
URL: https://github.com/HowardHinnant/date
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cmake >= 3.1.0
BuildRequires: gcc-c++ >= 5.3.1      

%define debug_package %{nil}

%description
Small date and time library with full iana tz database support

%package devel
Summary: Development files for date library

%description devel
Development files and cmake module for date library

%prep
%autosetup


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files devel
%license LICENSE.txt
%doc README.md
%{_libdir}/libtz.a
%{_libdir}/cmake/date/dateConfig.cmake
%{_includedir}/date/chrono_io.h
%{_includedir}/date/julian.h
%{_includedir}/date/tz_private.h
%{_includedir}/date/islamic.h
%{_includedir}/date/tz.h
%{_includedir}/date/date.h
%{_includedir}/date/iso_week.h
%{_includedir}/date/ios.h
%{_includedir}/date/ptz.h


%changelog
* Sun Jan 27 2019 Pablo Rodríguez González <pablo.rodriguez.gonzalez@gmail.com>
- Created SPEC file for RPM from Date version 2.4.1
