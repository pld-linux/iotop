Summary:	Top like utility for I/O
Summary(hu.UTF-8):	Top-szerű program I/O-hoz
Summary(pl.UTF-8):	Narzędzie podobne do topa dla I/O
Name:		iotop
Version:	0.6
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5ef9456b26d7694abf3101a72e1e0d1d
Patch0:		status-value-error.patch
Patch1:		python3.patch
URL:		http://guichaz.free.fr/iotop/
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python3
Requires:	python3-modules
Requires:	uname(release) >= 2.6.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command). iotop is a Python program
with a top like UI used to show of behalf of which process is the I/O
going on.

%description -l hu.UTF-8
A Linux mindig biztosította a lehetőségét annak, hogy figyelemmel
kövesd, mennyi I/O művelet zajlik (a bi és a bo oszlopa a vmstat 1
parancsnak). iotop egy Python program, top-szerű felülettel, amely a
processzek I/O műveleteit mutatja.

%description -l pl.UTF-8
Linux od zawsze był w stanie pokazać ilośc wykonywanych operacji we/wy
(kolumny bi i bo polecenia vmstat 1). iotop jest napisanym w języku
Python narzędziem z interfejsem zbliżonym do programu top,
wyświetlającym, dla których procesów wykonywane są operacje we/wy.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}

%py3_install

%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/iotop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS THANKS
%attr(755,root,root) %{_sbindir}/iotop
%{_mandir}/man8/iotop.8*
%{py3_sitescriptdir}/iotop
%{py3_sitescriptdir}/iotop-%{version}-py*.egg-info
