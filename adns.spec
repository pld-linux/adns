Name:		adns
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Version:	1.0
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_fix.patch
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
 - It is reasonably easy to use for simple programs which just want to
   translate names to addresses, look up MX records, etc.
 - It can be used in an asynchronous, non-blocking, manner. Many
   queries can be handled simultaneously.
 - Responses are decoded automatically into a natural representation
   for a C program - there is no need to deal with DNS packet formats.
 - Sanity checking (eg, name syntax checking, reverse/forward
   correspondence, CNAME pointing to CNAME) is performed automatically.
 - Time-to-live, CNAME and other similar information is returned in an
   easy-to-use form, without getting in the way.
 - There is no global state in the library; resolver state is an opaque
   data structure which the client creates explicitly. A program can have
   several instances of the resolver.
 - Errors are reported to the application in a way that distinguishes
   the various causes of failure properly.
 - Understands conventional resolv.conf, but this can overridden by
   environment variables.
 - Flexibility. For example, the application can tell adns to: ignore
   environment variables (for setuid programs), disable sanity checks eg
   to return arbitrary data, override or ignore resolv.conf in favour of
   supplied configuration, etc.
 - Believed to be correct ! For example, will correctly back off to TCP
   in case of long replies or queries, or to other nameservers if several
   are available. It has sensible handling of bad responses etc.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} >= %{version}

%description devel
Asynchronous-capable DNS client library - development files.

%package static
Summary:	Asynchronous-capable DNS client library - static library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} >= %{version}

%description static
Asynchronous-capable DNS client library - static library.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} >= %{version}

%description progs
DNS utility programs adns also comes with a number of utility programs
for use from the command line and in scripts:
 - adnslogres is a much faster version of Apache's logresolv program,
 - adnsresfilter is a filter which copies its input to its output,
   replacing IP addresses by the corresponding names, without unduly
   delaying the output. For example, you can usefully pipe the output of
   netstat -n, tcpdump -ln, and the like, into it.
 - adnshost is a general-purpose DNS lookup utility which can be used
   easily in from the command line and from shell scripts to do simple
   lookups. In a more advanced mode it can be used as a general-purpose
   DNS helper program for scripting languages which can invoke and
   communicate with subprocesses.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure \
	--enable-dynamic
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libadns.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libadns.so

gzip -9nf README TODO changelog
 
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
