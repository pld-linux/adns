Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Summary(pl):	Zaawansowana, prosta w u©yciu, asynchroniczna biblioteka kliencka DNS
Summary(ru):	Клиентская библиотека DNS с возможностью асинхронных запросов
Summary(uk):	Кл╕╓нтська б╕бл╕отека DNS з можлив╕стю асинхронних запит╕в
Name:		adns
Version:	1.3
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.gz
# Source0-md5:	d19cddcc11ce3183549bab7f136e0f73
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
BuildRequires:	autoconf
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
adns jest bibliotek╠ rozwi╠zywania nazw dla programСw w C (i C++). W
przeciwieЯstwie do pozostaЁych interfejsСw - gethostbyname itd. oraz
libresolv, ma nastЙpuj╠ce mo©liwo╤ci:
- Jest Ёatwa w u©yciu dla prostych programСw, ktСre maj╠ tylko
  tЁumaczyФ nazwy na adresy, szukaФ rekordСw MX itp.
- Mo©e byФ u©ywana w sposСb asynchroniczny, nieblokuj╠cy; wiele
  zapytaЯ mo©e byФ obsЁugiwanych jednocze╤nie.
- Odpowiedzi s╠ dekodowane automatycznie do reprezentacji naturalnej
  dla programСw w C - nie trzeba obsЁugiwaФ formatСw pakietСw DNS
- Sprawdzanie poprawno╤ci (skЁadni, zgodno╤ci rekordСw odwrotnych i
  prostych, CNAME wskazuj╠cych na CNAME) jest automatyczne.
- TTL, CNAME i podobne informacje s╠ zwracane w postaci Ёatwej do
  wykorzystania
- Nie ma globalnego stanu w bibliotece; stan resolvera jest struktur╠
  danych tworzon╠ przez klienta. Program mo©e trzymaФ wiele instancji
  resolvera.
- BЁЙdy s╠ zgЁaszane aplikacji w sposСb rozrС©niaj╠cy przyczyny.
- Rozumie konwencjonalny plik resolv.conf, ale to mo©e byФ zmienione
  przez zmienne ╤rodowiskowe.
- Konfigurowalno╤Ф. Na przykЁad aplikacja mo©e kazaФ adns: ignorowaФ
  zmienne ╤rodowiskowe (dla programСw setuid), wyЁ╠czyФ sprawdzanie
  poprawno╤ci, zignorowaФ resolv.conf na rzecz wЁasnej konfiguracji.
- Podobno jest poprawna! Na przykЁad, prawidЁowo przeЁ╠cza siЙ na TCP
  w przypadku dЁugich zapytaЯ lub odpowiedzi, albo na inne serwery je╤li
  jest kilka dostЙpnych. Ma rozs╠dn╠ obsЁugЙ zЁych odpowiedzi.

%description -l ru
adns - это библиотека резолвера для программ на C (и C++). В отличие
от существующих интерфейсов, gethostbyname с компанией и libresolv.
она имеет следующие возможности:
- Достаточно легкая для использования в простых программах, которым
  нужно всего лишь транслировать имена в адреса, искать MX записи, и
  т.п.
- Может использоваться асинхронным, неблокирующим способом. Множество
  запросов может обрабатываться одновременно.
- Ответы автоматически декодируются в естествееное для C программ
  представление - нет необходимости иметь дело с форматами DNS пакета.
- Проверка на корректность (например, проверка синтаксической
  допустимости имен, соответсвие обратного и прямого резолвинга, CNAME,
  указывающий на CNAME) выполняется автоматически.
- Время жизни записи (TTL), CNAME и другая подобная информация
  выдается в легкой для использования форме.
- Ошибки сообщаются приложению таким образом, что разные причины их
  возникновения различаются правильно.
- Понимает обычный resolv.conf, но это может быть изменено переменными
  среды.
- Гибкость. Например, программа может заказать adns: игнорировать
  переменные среды (для setuid программ), отключить проверки
  корректности для возврата данных такими, как они есть, игнорировать
  resolv.conf. пользуюсь собственной конфигурацией и т.п.
- Считается корректной! Например, корректно переключается на TCP в
  случае длинных ответов или запросов, или на другие сервера имен, если
  доступно несколько. Разбирается с некоректными ответами и т.д.

%description -l uk
adns - це б╕бл╕отека резолвера для програм на C (та C++). На в╕дм╕ну
в╕д ╕снуючих ╕нтерфейс╕в, gethostbyname з компан╕╓ю та libresolv, вона
ма╓ наступн╕ можливост╕:
- Досить легка для використання в простих програмах, як╕ лише
  транслюють ╕мена в адреси, шукають MX записи, тощо.
- Може використовуватись асинхронним, неблокуючим способом. Багато
  запит╕в можуть оброблятися одночасно.
- В╕дпов╕д╕ автоматично декодуються в природн╓ для C програм
  в╕дображення - нема╓ необх╕дност╕ мати справу з форматами DNS пакету.
- Перев╕рка на коректн╕сть (наприклад, перев╕рка синтаксично╖
  допустимост╕ ╕мен╕, в╕дпов╕дн╕сть зворотнього та прямого резолв╕нгу,
  CNAME, що вказу╓ на CNAME) викону╓ться автоматично.
- Час життя запису (TTL), CNAME та ╕нша под╕бна ╕нформац╕я вида╓ться в
  легк╕й для використання форм╕.
- Помилки пов╕домляються прикладн╕й програм╕ таким чином, що р╕зн╕
  причини ╖х виникнення розр╕зняються правильно.
- Розум╕╓ звичний resolv.conf, але це може бути в╕дм╕нено зм╕нними
  середовища.
- Гнучк╕сть. Наприклад, програма може замовити adns: ╕гнорувати зм╕нн╕
  середовища (для setuid програм), в╕дключити перев╕рки коректност╕ для
  повернення даних такими як вони ╓, ╕гнорувати resolv.conf,
  користуючись власною конф╕гурац╕╓ю та ╕н.
- Вважа╓ться коректною! Наприклад, коректно переключа╓ться на TCP у
  випадку довгих в╕дпов╕дей чи запит╕в, чи на ╕нш╕ сервери ╕мен, коли
  доступно к╕лька. Розбира╓ться з некоректними в╕дпов╕дями та ╕н.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - pliki dla programistСw
Summary(ru):	Файлы для разработки с использованием библиотеки adns
Summary(uk):	Файли для розробки з використанням б╕бл╕отеки adns
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Asynchronous-capable DNS client library - development files.

%description devel -l pl
Asynchroniczna biblioteka kliencka DNS - pliki dla programistСw.

%description devel -l ru
adns - это библиотека резолвера для программ на C (и C++). Этот пакет
содержит файлы, необходимые для разработки программ.

%description devel -l uk
adns - це б╕бл╕отека резолвера для програм на C (та C++). Цей пакет
м╕стить файли, необх╕дн╕ для розробки програм.

%package static
Summary:	Asynchronous-capable DNS client library - static library
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - wersja statyczna
Summary(ru):	Статические библиотеки для разработки с использованием библиотеки adns
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки з використанням б╕бл╕отеки adns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Asynchronous-capable DNS client library - static library.

%description static -l pl
Asynchroniczna biblioteka kliencka DNS - biblioteka statyczna.

%description static -l ru
adns - это библиотека резолвера для программ на C (и C++). Этот пакет
содержит статические библиотеки для разработки программ.

%description static -l uk
adns - це б╕бл╕отека резолвера для програм на C (та C++). Цей пакет
м╕стить статичн╕ б╕б╕л╕отеки для розробки програм.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - narzЙdzia
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
NarzЙdzia DNS: adns przychodzi z paroma programami narzЙdziowymi do
u©ytku z linii poleceЯ lub w skryptach:
- adnslogres to o wiele szybsza wersja programu logresolv z Apache
- adnsresfilter to filtr kopiuj╠cy wej╤cie na wyj╤cie zamieniaj╠c
  adresy IP na nazwy, bez niepotrzebnych opС╪nieЯ. Na przykЁad mo©esz na
  wej╤cie wpu╤ciФ wyj╤cie z netstat -n, tcpdump -ln itp.
- adnshost to ogСlnego przeznaczenia narzЙdzie do odpytywania DNS,
  proste w u©yciu z linii poleceЯ i skryptСw powЁoki.

%prep
%setup -q
%patch0 -p1

%build
# aclocal.m4 is only local, don't run aclocal
%{__autoconf}
%configure \
	--enable-dynamic
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libadns.so.*.* libadns.so

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO changelog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
