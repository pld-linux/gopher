Summary:	gopher client
Summary(pl):	Klient protoko³u gopher
Name:		gopher
Version:	3.0.5
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		John Goerzen <jgoerzen@complete.org>
Source0:	http://gopher.quux.org:70/give-me-gopher/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		gopher://gopher.quux.org/1/Software/Gopher
#BuildRequires:	-
#PreReq:		-
#Requires:	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gopher client is used to talk to gopher servers.

%description -l pl
Klient protoko³u gopher s³u¿y do ³±czenia siê z serwerami gophera.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copyright README doc/{FAQ,PLATFORMS,TODO} doc/[cgo]*.changes doc/gindexd.doc
%doc announcements/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man[58]/gopher[^d]*

#%files subpackage
#%defattr(644,root,root,755)
#%doc doc/server.*
#%attr(755,root,root) %{_bindir}/gopherd
#%%{_mandir}/man[58]/gopherd*
