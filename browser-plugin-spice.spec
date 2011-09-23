Summary:	Spice-XPI plugin for Mozilla compatible browsers
Summary(pl.UTF-8):	Wtyczka Spice-XPI dla przeglądarek WWW kompatybilnych z Mozillą
Name:		browser-plugin-spice
Version:	2.6
Release:	0.1
License:	MPL v1.1 or GPL v2.0 or LGPL v2.1
Group:		X11/Applications
Source0:	http://spice-space.org/download/releases/spice-xpi-%{version}.tar.bz2
# Source0-md5:	e1099df16c66a762c2cc176c39ff8561
Patch0:		spice-xpi-sh.patch
URL:		http://spice-space.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	log4cpp-devel
BuildRequires:	nspr-devel >= 4.7.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xulrunner-devel >= 1.9.1
Requires:	browser-plugins >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spice-XPI plugin for Mozilla compatible browsers.

%description -l pl.UTF-8
Wtyczka Spice-XPI dla przeglądarek WWW kompatybilnych z Mozillą.

%prep
%setup -q -n spice-xpi-%{version}
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_browserpluginsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_browserpluginsdir}

install SpiceXPI/src/plugin/nsISpicec.xpt $RPM_BUILD_ROOT%{_browserpluginsdir}
%{__rm} $RPM_BUILD_ROOT%{_browserpluginsdir}/libnsISpicec.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_browserpluginsdir}/libnsISpicec.so
%{_browserpluginsdir}/nsISpicec.xpt
%{_datadir}/spice
