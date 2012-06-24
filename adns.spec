Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Summary(pl):	Zaawansowana, prosta w u�yciu, asynchroniczna biblioteka kliencka DNS
Summary(ru):	���������� ���������� DNS � ������������ ����������� ��������
Summary(uk):	�̦������� ¦�̦����� DNS � �����צ��� ����������� ����Ԧ�
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
adns jest bibliotek� rozwi�zywania nazw dla program�w w C (i C++). W
przeciwie�stwie do pozosta�ych interfejs�w - gethostbyname itd. oraz
libresolv, ma nast�puj�ce mo�liwo�ci:
- Jest �atwa w u�yciu dla prostych program�w, kt�re maj� tylko
  t�umaczy� nazwy na adresy, szuka� rekord�w MX itp.
- Mo�e by� u�ywana w spos�b asynchroniczny, nieblokuj�cy; wiele
  zapyta� mo�e by� obs�ugiwanych jednocze�nie.
- Odpowiedzi s� dekodowane automatycznie do reprezentacji naturalnej
  dla program�w w C - nie trzeba obs�ugiwa� format�w pakiet�w DNS
- Sprawdzanie poprawno�ci (sk�adni, zgodno�ci rekord�w odwrotnych i
  prostych, CNAME wskazuj�cych na CNAME) jest automatyczne.
- TTL, CNAME i podobne informacje s� zwracane w postaci �atwej do
  wykorzystania
- Nie ma globalnego stanu w bibliotece; stan resolvera jest struktur�
  danych tworzon� przez klienta. Program mo�e trzyma� wiele instancji
  resolvera.
- B��dy s� zg�aszane aplikacji w spos�b rozr�niaj�cy przyczyny.
- Rozumie konwencjonalny plik resolv.conf, ale to mo�e by� zmienione
  przez zmienne �rodowiskowe.
- Konfigurowalno��. Na przyk�ad aplikacja mo�e kaza� adns: ignorowa�
  zmienne �rodowiskowe (dla program�w setuid), wy��czy� sprawdzanie
  poprawno�ci, zignorowa� resolv.conf na rzecz w�asnej konfiguracji.
- Podobno jest poprawna! Na przyk�ad, prawid�owo prze��cza si� na TCP
  w przypadku d�ugich zapyta� lub odpowiedzi, albo na inne serwery je�li
  jest kilka dost�pnych. Ma rozs�dn� obs�ug� z�ych odpowiedzi.

%description -l ru
adns - ��� ���������� ��������� ��� �������� �� C (� C++). � �������
�� ������������ �����������, gethostbyname � ��������� � libresolv.
��� ����� ��������� �����������:
- ���������� ������ ��� ������������� � ������� ����������, �������
  ����� ����� ���� ������������� ����� � ������, ������ MX ������, �
  �.�.
- ����� �������������� �����������, ������������� ��������. ���������
  �������� ����� �������������� ������������.
- ������ ������������� ������������ � ������������ ��� C ��������
  ������������� - ��� ������������� ����� ���� � ��������� DNS ������.
- �������� �� ������������ (��������, �������� ��������������
  ������������ ����, ����������� ��������� � ������� ����������, CNAME,
  ����������� �� CNAME) ����������� �������������.
- ����� ����� ������ (TTL), CNAME � ������ �������� ����������
  �������� � ������ ��� ������������� �����.
- ������ ���������� ���������� ����� �������, ��� ������ ������� ��
  ������������� ����������� ���������.
- �������� ������� resolv.conf, �� ��� ����� ���� �������� �����������
  �����.
- ��������. ��������, ��������� ����� �������� adns: ������������
  ���������� ����� (��� setuid ��������), ��������� ��������
  ������������ ��� �������� ������ ������, ��� ��� ����, ������������
  resolv.conf. ��������� ����������� ������������� � �.�.
- ��������� ����������! ��������, ��������� ������������� �� TCP �
  ������ ������� ������� ��� ��������, ��� �� ������ ������� ����, ����
  �������� ���������. ����������� � ������������ �������� � �.�.

%description -l uk
adns - �� ¦�̦����� ��������� ��� ������� �� C (�� C++). �� צ�ͦ��
צ� �������� ��������Ӧ�, gethostbyname � �����Φ�� �� libresolv, ����
��� ������Φ ��������Ԧ:
- ������ ����� ��� ������������ � ������� ���������, �˦ ����
  ���������� ����� � ������, ������� MX ������, ����.
- ���� ����������������� �����������, ����������� ��������. ������
  ����Ԧ� ������ ����������� ���������.
- �����צĦ ����������� ����������� � ������Τ ��� C �������
  צ���������� - ����� ����Ȧ����Ԧ ���� ������ � ��������� DNS ������.
- ����צ��� �� ������Φ��� (���������, ����צ��� ����������ϧ
  ����������Ԧ ���Φ, צ���צ�Φ��� ����������� �� ������� �����צ���,
  CNAME, �� ����դ �� CNAME) �����դ���� �����������.
- ��� ����� ������ (TTL), CNAME �� ���� ��Ħ��� �������æ� ��������� �
  ���˦� ��� ������������ ���ͦ.
- ������� ��צ���������� �������Φ� ������ͦ ����� �����, �� Ҧ�Φ
  ������� �� ���������� ���Ҧ�������� ���������.
- ����ͦ� ������� resolv.conf, ��� �� ���� ���� צ�ͦ���� �ͦ�����
  ����������.
- ����˦���. ���������, �������� ���� �������� adns: ���������� �ͦ�Φ
  ���������� (��� setuid �������), צ�������� ����צ��� ���������Ԧ ���
  ���������� ����� ������ �� ���� �, ���������� resolv.conf,
  ������������ ������� ���Ʀ����æ�� �� ��.
- ���������� ���������! ���������, �������� �������������� �� TCP �
  ������� ������ צ���צ��� �� ����Ԧ�, �� �� ��ۦ ������� ����, ����
  �������� ˦����. ������������ � ������������ צ���צ���� �� ��.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - pliki dla programist�w
Summary(ru):	����� ��� ���������� � �������������� ���������� adns
Summary(uk):	����� ��� �������� � ������������� ¦�̦����� adns
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Asynchronous-capable DNS client library - development files.

%description devel -l pl
Asynchroniczna biblioteka kliencka DNS - pliki dla programist�w.

%description devel -l ru
adns - ��� ���������� ��������� ��� �������� �� C (� C++). ���� �����
�������� �����, ����������� ��� ���������� ��������.

%description devel -l uk
adns - �� ¦�̦����� ��������� ��� ������� �� C (�� C++). ��� �����
ͦ����� �����, ����Ȧ�Φ ��� �������� �������.

%package static
Summary:	Asynchronous-capable DNS client library - static library
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - wersja statyczna
Summary(ru):	����������� ���������� ��� ���������� � �������������� ���������� adns
Summary(uk):	������Φ ¦�̦����� ��� �������� � ������������� ¦�̦����� adns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Asynchronous-capable DNS client library - static library.

%description static -l pl
Asynchroniczna biblioteka kliencka DNS - biblioteka statyczna.

%description static -l ru
adns - ��� ���������� ��������� ��� �������� �� C (� C++). ���� �����
�������� ����������� ���������� ��� ���������� ��������.

%description static -l uk
adns - �� ¦�̦����� ��������� ��� ������� �� C (�� C++). ��� �����
ͦ����� ������Φ ¦¦̦����� ��� �������� �������.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Summary(pl):	Asynchroniczna biblioteka kliencka DNS - narz�dzia
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
Narz�dzia DNS: adns przychodzi z paroma programami narz�dziowymi do
u�ytku z linii polece� lub w skryptach:
- adnslogres to o wiele szybsza wersja programu logresolv z Apache
- adnsresfilter to filtr kopiuj�cy wej�cie na wyj�cie zamieniaj�c
  adresy IP na nazwy, bez niepotrzebnych op�nie�. Na przyk�ad mo�esz na
  wej�cie wpu�ci� wyj�cie z netstat -n, tcpdump -ln itp.
- adnshost to og�lnego przeznaczenia narz�dzie do odpytywania DNS,
  proste w u�yciu z linii polece� i skrypt�w pow�oki.

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
