Summary:	Top like utility for I/O
Summary(hu.UTF-8):	Top-szerű program I/O-hoz
Summary(pl.UTF-8):	Narzędzie podobne do topa dla I/O
Name:		iotop
Version:	0.4
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3607f8b77ed6686efd9a4a7e6c135ceb
URL:		http://guichaz.free.fr/iotop/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python >= 1:2.5
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
Linux od zawsze był w stanie pokazać zużycie I/O (kolumny bi i bo
polecenia vmstat 1). iotop jest napisanym w języku Python narzędziem z
interfejsem zbliżonym do top wyświetlającym zużycie I/O poszczególnych
procesów.

%prep
%setup -q

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python ./setup.py install \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

install iotop.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS THANKS
%attr(755,root,root) %{_bindir}/iotop
%{py_sitescriptdir}/iotop
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/iotop.1*
