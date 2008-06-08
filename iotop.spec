Summary:	Top like utility for I/O
Summary(pl.UTF-8):	Narzędzie podobne do topa dla I/O
Name:		iotop
Version:	0.2
Release:	1
License:	GPLv2
Group:		Applications/System
Source0:	http://guichaz.free.fr/iotop/files/iotop-0.2.tar.bz2
# Source0-md5:	b506e34c7b292f7bb7111b9ed67f68ea
URL:		http://guichaz.free.fr/iotop/
%pyrequires_eq	python-modules
BuildRequires:	python-devel
Requires:	python >= 1:2.5
Requires:	uname(release) >= 2.6.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command). iotop is a Python program
with a top like UI used to show of behalf of which process is the I/O
going on.

%prep
%setup -q

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
        --single-version-externally-managed \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iotop
%{py_sitescriptdir}/iotop
%{py_sitescriptdir}/*.egg-info
