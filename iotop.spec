Summary:	Top like utility for I/O
Summary(pl.UTF-8):Narzędzie podobne do topa dla I/O
Name:		iotop
Version:	0.1
Release:	0.1
License:	GPLv2
Group:		Applications/System
Source0:	http://guichaz.free.fr/misc/%{name}.py
# Source0-md5:	ed93de5cfc193e62c5ab0101fb8f61c1
Patch0:		xterm-color-fix.patch
URL:		http://guichaz.free.fr/misc/#iotop
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command). iotop is a Python program
with a top like UI used to show of behalf of which process is the I/O
going on.

%prep
cp -p %{SOURCE0} .
%patch0 -p0 -b .xterm-color

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p iotop.py $RPM_BUILD_ROOT%{_bindir}/iotop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iotop
