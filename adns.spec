# (fg) 20010103 Library stuff
%define libmajor 1
%define libname libadns%{libmajor}

Name:		adns
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Version:	1.0
Release:	6mdk
License:	GPL
Group:		Networking/Other
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
Source:		ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
Prefix:		%{_prefix}
Requires: 	%{libname} = %{version}

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
    * It is reasonably easy to use for simple programs which just want
      to translate names to addresses, look up MX records, etc.
    * It can be used in an asynchronous, non-blocking, manner. Many
      queries can be handled simultaneously.
    * Responses are decoded automatically into a natural representation
      for a C program - there is no need to deal with DNS packet
      formats.
    * Sanity checking (eg, name syntax checking, reverse/forward
      correspondence, CNAME pointing to CNAME) is performed
      automatically.
    * Time-to-live, CNAME and other similar information is returned in
      an easy-to-use form, without getting in the way.
    * There is no global state in the library; resolver state is an
      opaque data structure which the client creates explicitly. A
      program can have several instances of the resolver.
    * Errors are reported to the application in a way that distinguishes
      the various causes of failure properly.
    * Understands conventional resolv.conf, but this can overridden by
      environment variables.
    * Flexibility. For example, the application can tell adns to: ignore
      environment variables (for setuid programs), disable sanity checks
      eg to return arbitrary data, override or ignore resolv.conf in
      favour of supplied configuration, etc.
    * Believed to be correct ! For example, will correctly back off to
      TCP in case of long replies or queries, or to other nameservers if
      several are available. It has sensible handling of bad responses
      etc.

%package -n %{libname}
Group:	System/Libraries
Summary: Libraries needed to run applications using adns.

%description -n %{libname}
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
    * It is reasonably easy to use for simple programs which just want
      to translate names to addresses, look up MX records, etc.
    * It can be used in an asynchronous, non-blocking, manner. Many
      queries can be handled simultaneously.
    * Responses are decoded automatically into a natural representation
      for a C program - there is no need to deal with DNS packet
      formats.
    * Sanity checking (eg, name syntax checking, reverse/forward
      correspondence, CNAME pointing to CNAME) is performed
      automatically.
    * Time-to-live, CNAME and other similar information is returned in
      an easy-to-use form, without getting in the way.
    * There is no global state in the library; resolver state is an
      opaque data structure which the client creates explicitly. A
      program can have several instances of the resolver.
    * Errors are reported to the application in a way that distinguishes
      the various causes of failure properly.
    * Understands conventional resolv.conf, but this can overridden by
      environment variables.
    * Flexibility. For example, the application can tell adns to: ignore
      environment variables (for setuid programs), disable sanity checks
      eg to return arbitrary data, override or ignore resolv.conf in
      favour of supplied configuration, etc.
    * Believed to be correct ! For example, will correctly back off to
      TCP in case of long replies or queries, or to other nameservers if
      several are available. It has sensible handling of bad responses
      etc.

This package contains all of adns libraries.

%package -n %{libname}-devel
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Group:	Development/C
Requires: %{libname} = %{version}
Provides: libadns-devel
Obsoletes: adns-devel

%description -n %{libname}-devel
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
    * It is reasonably easy to use for simple programs which just want
      to translate names to addresses, look up MX records, etc.
    * It can be used in an asynchronous, non-blocking, manner. Many
      queries can be handled simultaneously.
    * Responses are decoded automatically into a natural representation
      for a C program - there is no need to deal with DNS packet
      formats.
    * Sanity checking (eg, name syntax checking, reverse/forward
      correspondence, CNAME pointing to CNAME) is performed
      automatically.
    * Time-to-live, CNAME and other similar information is returned in
      an easy-to-use form, without getting in the way.
    * There is no global state in the library; resolver state is an
      opaque data structure which the client creates explicitly. A
      program can have several instances of the resolver.
    * Errors are reported to the application in a way that distinguishes
      the various causes of failure properly.
    * Understands conventional resolv.conf, but this can overridden by
      environment variables.
    * Flexibility. For example, the application can tell adns to: ignore
      environment variables (for setuid programs), disable sanity checks
      eg to return arbitrary data, override or ignore resolv.conf in
      favour of supplied configuration, etc.
    * Believed to be correct ! For example, will correctly back off to
      TCP in case of long replies or queries, or to other nameservers if
      several are available. It has sensible handling of bad responses
      etc.

This package contains static libraries and header files need for development.

%prep

%setup -q

%build
%configure
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix %{_prefix}
%make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}

%makeinstall

#make prefix=$RPM_BUILD_ROOT%{_prefix} install
(set -e
 cd $RPM_BUILD_ROOT%{_libdir}
 ln -s libadns.so.? libadns.so
)
 
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README TODO changelog
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog

* Wed Jul 18 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0-6mdk

- Submit SRPM this time...
- Changes in -5mdk were:
  * recompile to get correct distrib tag
  * use -p in %%post{,un}
  * s,Copyright,License,
  * fixed summary-too-long error

* Thu Jan 04 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0-4mdk

- libadns1-devel obsoletes adns-devel - lart me again

* Wed Jan 03 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0-3mdk

- Gee, what a crotch! Forgot to submit the source RPM...

* Wed Jan 03 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0-2mdk

- Follow policy for libraries
- Don't use macros when not needed

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-1mdk
- new and shiny release.

* Fri Jul 21 2000 Warly <warly@mandrakesoft.com> 0.8-1mdk
- new release

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.7-4mdk
- Definitively remove the make check (stupid).

* Sun May 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7-3mdk
- Work around for i486
- Fix prefix
- Use %%{_tmppath} for BuildRoot

* Thu Mar 23 2000 Florent Villard <warly@mandrakesoft.com> 0.7-2mdk
- rebuild

* Fri Mar  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.7-1mdk
- 0.7.
- clean spec and split in 2 packages.

* Mon Feb 07 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Sun Jan 30 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
