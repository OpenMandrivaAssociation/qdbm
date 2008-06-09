%define version   1.8.77
%define release   %mkrel 2

%define major 14
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		qdbm
Summary:	Quick Database Manager
Version:	%{version}
Release:	%{release}
Group:		Databases
License:	LGPL
URL:		http://qdbm.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	zlib

%description
QDBM is an embeded database library compatible 
with GDBM and NDBM.
It features hash database and B+ tree database and 
is developed referring to GDBM for the purpose of the 
following three points: higher processing
speed, smaller size of a database file, and simpler API.
This package includes APIs for C, C++, and Java.
CGI scripts are also contained. APIs for Perl and Ruby 
should be installed with a source package.


%package -n %{libname}
Summary:	QDBM library
Group:		Databases

%description -n %{libname}
QDBM library.

%package -n %{develname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d qdbm 14
Conflicts:	%libname < 1.8.77-2

%description -n %{develname}
QDBM development package: static libraries, header files, and the like.


%prep
%setup -q

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove docs (they should be installed by %doc)
rm -f $RPM_BUILD_ROOT/%{_datadir}/qdbm/{COPYING,ChangeLog,NEWS,THANKS,*.html}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README THANKS
%doc spex.html spex-ja.html
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/libqdbm.a
%{_libdir}/pkgconfig/qdbm.pc
