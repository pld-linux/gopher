Summary:	gopher client
Summary(pl):	Klient protoko³u gopher
Name:		gopher
Version:	3.0.5
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		John Goerzen <jgoerzen@complete.org>
Source0:	http://gopher.quux.org:70/give-me-gopher/%{name}-%{version}.tar.gz
# Source0-md5:	1527f94ba8538a2d029155844195bba8
Patch0:		%{name}-ac.patch
URL:		gopher://gopher.quux.org/1/Software/Gopher
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gopher client is used to talk to gopher servers.

%description -l pl
Klient protoko³u gopher s³u¿y do ³±czenia siê z serwerami gophera.

%package server
Summary:	gopherd - a gopher server
Summary(pl):	gopherd - serwer gophera
Group:		Networking/Daemons

%description server
gopherd - a gopher server.

%description server -l pl
gopherd - serwer gophera.

%prep
%setup -q
%patch0 -p1

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
%doc copyright README doc/{FAQ,PLATFORMS,TODO} doc/[cgo]*.changes doc/gindexd.doc
%doc announcements/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/gopher
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopher.hlp
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopher.rc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopherremote.rc
%{_mandir}/man1/*
%{_mandir}/man5/gopherrc.5*

%files server
%defattr(644,root,root,755)
%doc doc/server.*
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/gopherd
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopherd/gopherd.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopherd/gopherdlocal.conf
%{_mandir}/man5/gopherd.conf.5*
%{_mandir}/man8/*
