Summary:	gopher client
Summary(pl.UTF-8):	Klient protokołu gopher
Name:		gopher
Version:	3.0.6
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		John Goerzen <jgoerzen@complete.org>
Source0:	http://gopher.quux.org:70/give-me-gopher/%{name}_%{version}.tar.gz
# Source0-md5:	0cffe1ec0e3e5600af1fe590db852c12
Patch0:		%{name}-ac.patch
Patch1:		%{name}-gcc4.patch
URL:		gopher://gopher.quux.org/1/Software/Gopher
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gopher client is used to talk to gopher servers.

%description -l pl.UTF-8
Klient protokołu gopher służy do łączenia się z serwerami gophera.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man{1,5,8}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MAN5DIR=$RPM_BUILD_ROOT%{_mandir}/man5 \
	MAN8DIR=$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copyright README doc/{FAQ,PLATFORMS,TODO} doc/[cgo]*.changes
%doc announcements/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/gopher
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gopher/gopher.hlp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gopher/gopher.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gopher/gopherremote.rc
%{_mandir}/man1/*
%{_mandir}/man5/gopherrc.5*
