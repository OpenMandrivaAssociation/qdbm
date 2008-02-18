%define version   1.8.75
%define release   %mkrel 1

%define libname_orig lib%{name}
%define libname %mklibname %{name} 14

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
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
QDBM library.

%package -n %{libname}-devel
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README THANKS
%doc spex.html spex-ja.html
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libqdbm.a
%{_libdir}/pkgconfig/qdbm.pc


