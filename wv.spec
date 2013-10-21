Summary:	MSWord document parsing library and tools
Name:		wv
Version:	1.2.9
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.abisource.com/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	dbccf2e9f747e50c913b7e3d126b73f7
URL:		http://wvware.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libgsf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wv is a suite of programs to help convert Word Documents to HTML.

%package libs
Summary:	wv library
Group:		Libraries

%description libs
wv library.

%package devel
Summary:	Include files needed to compile
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxml2-devel
Requires:	zlib-devel

%description devel
Contains the header files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/wv*
%{_datadir}/wv
%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libwv-*.so.?
%attr(755,root,root) %{_libdir}/libwv-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwv.so
%{_includedir}/wv
%{_pkgconfigdir}/wv-*.pc

