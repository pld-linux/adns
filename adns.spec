Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Summary(pl.UTF-8):	Zaawansowana, prosta w użyciu, asynchroniczna biblioteka kliencka DNS
Summary(ru.UTF-8):	Клиентская библиотека DNS с возможностью асинхронных запросов
Summary(uk.UTF-8):	Клієнтська бібліотека DNS з можливістю асинхронних запитів
Name:		adns
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.gz
# Source0-md5:	88bc7bbf3f62a8d4fb186b8f72ead853
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

%description -l pl.UTF-8
adns jest biblioteką rozwiązywania nazw dla programów w C (i C++). W
przeciwieństwie do pozostałych interfejsów - gethostbyname itd. oraz
libresolv, ma następujące możliwości:
- Jest łatwa w użyciu dla prostych programów, które mają tylko
  tłumaczyć nazwy na adresy, szukać rekordów MX itp.
- Może być używana w sposób asynchroniczny, nieblokujący; wiele
  zapytań może być obsługiwanych jednocześnie.
- Odpowiedzi są dekodowane automatycznie do reprezentacji naturalnej
  dla programów w C - nie trzeba obsługiwać formatów pakietów DNS
- Sprawdzanie poprawności (składni, zgodności rekordów odwrotnych i
  prostych, CNAME wskazujących na CNAME) jest automatyczne.
- TTL, CNAME i podobne informacje są zwracane w postaci łatwej do
  wykorzystania
- Nie ma globalnego stanu w bibliotece; stan resolvera jest strukturą
  danych tworzoną przez klienta. Program może trzymać wiele instancji
  resolvera.
- Błędy są zgłaszane aplikacji w sposób rozróżniający przyczyny.
- Rozumie konwencjonalny plik resolv.conf, ale to może być zmienione
  przez zmienne środowiskowe.
- Konfigurowalność. Na przykład aplikacja może kazać adns: ignorować
  zmienne środowiskowe (dla programów setuid), wyłączyć sprawdzanie
  poprawności, zignorować resolv.conf na rzecz własnej konfiguracji.
- Podobno jest poprawna! Na przykład, prawidłowo przełącza się na TCP
  w przypadku długich zapytań lub odpowiedzi, albo na inne serwery jeśli
  jest kilka dostępnych. Ma rozsądną obsługę złych odpowiedzi.

%description -l ru.UTF-8
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

%description -l uk.UTF-8
adns - це бібліотека резолвера для програм на C (та C++). На відміну
від існуючих інтерфейсів, gethostbyname з компанією та libresolv, вона
має наступні можливості:
- Досить легка для використання в простих програмах, які лише
  транслюють імена в адреси, шукають MX записи, тощо.
- Може використовуватись асинхронним, неблокуючим способом. Багато
  запитів можуть оброблятися одночасно.
- Відповіді автоматично декодуються в природнє для C програм
  відображення - немає необхідності мати справу з форматами DNS пакету.
- Перевірка на коректність (наприклад, перевірка синтаксичної
  допустимості імені, відповідність зворотнього та прямого резолвінгу,
  CNAME, що вказує на CNAME) виконується автоматично.
- Час життя запису (TTL), CNAME та інша подібна інформація видається в
  легкій для використання формі.
- Помилки повідомляються прикладній програмі таким чином, що різні
  причини їх виникнення розрізняються правильно.
- Розуміє звичний resolv.conf, але це може бути відмінено змінними
  середовища.
- Гнучкість. Наприклад, програма може замовити adns: ігнорувати змінні
  середовища (для setuid програм), відключити перевірки коректності для
  повернення даних такими як вони є, ігнорувати resolv.conf,
  користуючись власною конфігурацією та ін.
- Вважається коректною! Наприклад, коректно переключається на TCP у
  випадку довгих відповідей чи запитів, чи на інші сервери імен, коли
  доступно кілька. Розбирається з некоректними відповідями та ін.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Summary(pl.UTF-8):	Asynchroniczna biblioteka kliencka DNS - pliki dla programistów
Summary(ru.UTF-8):	Файлы для разработки с использованием библиотеки adns
Summary(uk.UTF-8):	Файли для розробки з використанням бібліотеки adns
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Asynchronous-capable DNS client library - development files.

%description devel -l pl.UTF-8
Asynchroniczna biblioteka kliencka DNS - pliki dla programistów.

%description devel -l ru.UTF-8
adns - это библиотека резолвера для программ на C (и C++). Этот пакет
содержит файлы, необходимые для разработки программ.

%description devel -l uk.UTF-8
adns - це бібліотека резолвера для програм на C (та C++). Цей пакет
містить файли, необхідні для розробки програм.

%package static
Summary:	Asynchronous-capable DNS client library - static library
Summary(pl.UTF-8):	Asynchroniczna biblioteka kliencka DNS - wersja statyczna
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием библиотеки adns
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням бібліотеки adns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Asynchronous-capable DNS client library - static library.

%description static -l pl.UTF-8
Asynchroniczna biblioteka kliencka DNS - biblioteka statyczna.

%description static -l ru.UTF-8
adns - это библиотека резолвера для программ на C (и C++). Этот пакет
содержит статические библиотеки для разработки программ.

%description static -l uk.UTF-8
adns - це бібліотека резолвера для програм на C (та C++). Цей пакет
містить статичні бібіліотеки для розробки програм.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Summary(pl.UTF-8):	Asynchroniczna biblioteka kliencka DNS - narzędzia
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

%description progs -l pl.UTF-8
Narzędzia DNS: adns przychodzi z paroma programami narzędziowymi do
użytku z linii poleceń lub w skryptach:
- adnslogres to o wiele szybsza wersja programu logresolv z Apache
- adnsresfilter to filtr kopiujący wejście na wyjście zamieniając
  adresy IP na nazwy, bez niepotrzebnych opóźnień. Na przykład możesz na
  wejście wpuścić wyjście z netstat -n, tcpdump -ln itp.
- adnshost to ogólnego przeznaczenia narzędzie do odpytywania DNS,
  proste w użyciu z linii poleceń i skryptów powłoki.

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
