Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Summary(pl):	Zaawansowana, prosta w uøyciu, asynchroniczna biblioteka kliencka DNS
Name:		adns
Version:	1.0
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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

%description -l pl
adns jest bibliotek± rozwi±zywania nazw dla programÛw w C (i C++). W
przeciwieÒstwie do pozosta≥ych interfejsÛw - gethostbyname itd. oraz
libresolv, ma nastÍpuj±ce moøliwo∂ci:
 - Jest ≥atwa w uøyciu dla prostych programÛw, ktÛre maj± tylko
   t≥umaczyÊ nazwy na adresy, szukaÊ rekordÛw MX itp.
 - Moøe byÊ uøywana w sposÛb asynchroniczny, nieblokuj±cy; wiele
   zapytaÒ moøe byÊ obs≥ugiwanych jednocze∂nie.
 - Odpowiedzi s± dekodowane automatycznie do reprezentacji naturalnej
   dla programÛw w C - nie trzeba obs≥ugiwaÊ formatÛw pakietÛw DNS
 - Sprawdzanie poprawno∂ci (sk≥adni, zgodno∂ci rekordÛw odwrotnych i
   prostych, CNAME wskazuj±cych na CNAME) jest automatyczne.
 - TTL, CNAME i podobne informacje s± zwracane w postaci ≥atwej do
   wykorzystania
 - Nie ma globalnego stanu w bibliotece; stan resolvera jest struktur±
   danych tworzon± przez klienta. Program moøe trzymaÊ wiele intancji
   resolvera.
 - B≥Ídy s± zg≥aszane aplikacji w sposÛb rozrÛøniaj±cy przyczyny.
 - Rozumie konwencjonalny plik resolv.conf, ale to moøe byÊ zmienione
   przez zmienne ∂rodowiskowe.
 - Konfigurowalno∂Ê. Na przyk≥ad aplikacja moøe kazaÊ adns: ignorowaÊ
   zmienne ∂rodowiskowe (dla programÛw setuid), wy≥±czyÊ sprawdzanie
   poprawno∂ci, zignorowaÊ resolv.conf na rzecz w≥asnej konfiguracji.
 - Podobno jest poprawna! Na przyk≥ad, prawid≥owo prze≥±cza siÍ na TCP
   w przypadku d≥ugich zapytaÒ lub odpowiedzi, albo na inne serwery je∂li
   jest kilka dostÍpnych. Ma rozs±dn± obs≥ugÍ z≥ych odpowiedzi.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - pliki dla programistÛw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Asynchronous-capable DNS client library - development files.

%description devel -l pl
Asynchroniczna biblioteka kliencka DNS - pliki dla programistÛw.

%package static
Summary:	Asynchronous-capable DNS client library - static library
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - wersja statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
Asynchronous-capable DNS client library - static library.

%description static -l pl
Asynchroniczna biblioteka kliencka DNS - biblioteka statyczna.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - narzÍdzia
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description progs
DNS utility programs: adns also comes with a number of utility
programs for use from the command line and in scripts:
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

%description progs -l pl
NarzÍdzia DNS: adns przychodzi z paroma programami narzÍdziowymi do
uøytku z linii poleceÒ lub w skryptach:
 - adnslogres to o wiele szybsza wersja programu logresolv z Apache
 - adnsresfilter to filtr kopiuj±cy wej∂cie na wyj∂cie zamieniaj±c
   adresy IP na nazwy, bez niepotrzebnych opÛºnieÒ. Na przyk≥ad moøesz na
   werj∂cie wpu∂ciÊ wyj∂cie z netstat -n, tcpdump -ln itp.
 - adnshost to ogÛlnego przeznaczenia narzÍdzie do odpytywania DNS,
   proste w uøyciu z linii poleceÒ i skryptÛw pow≥oki.

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
 
%clean
rm -fr $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
