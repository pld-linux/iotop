Summary:	Top like utility for I/O
Summary(pl.UTF-8):	Narzędzie podobne do topa dla I/O
Name:		iotop
Version:	0.1
Release:	2
License:	GPLv2
Group:		Applications/System
Source0:	http://guichaz.free.fr/misc/%{name}.py
# Source0-md5:	ed93de5cfc193e62c5ab0101fb8f61c1
Patch0:		%{name}-ncurses.patch
URL:		http://guichaz.free.fr/misc/#iotop
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
%setup -q -c -T
cp -a %{SOURCE0} .
%patch0 -p0 -b .xterm-color

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install iotop.py $RPM_BUILD_ROOT%{_bindir}/iotop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iotop
