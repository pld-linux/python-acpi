%include	/usr/lib/rpm/macros.python

%define         module acpi

Summary:	Module for manipulating ID3 informational tags on MP3 audio files
Summary(pl):	Modu³ s³u¿±cy do manipulacji znacznikami ID3 plików MP3
Name:		python-%{module}
Version:	0.1.0
Release:	1
License:	Custom
Group:		Development/Languages/Python
Source0:	http://www.iapp.de/~riemer/projects/acpi.py/%{module}.py-%{version}-0-generic-src.tgz
# Source0-md5:	7145fd5eca938f214a165f441c0ba96d
Source1:	%{name}-setup.py
Patch0:		%{name}-bugfix.patch
URL:		http://www.iapp.de/~riemer/projects/acpi.py/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of acpi.py is providing of an uniform and platform
independent interface to ACPI. At the moment it implements only
battery relevant functions. The interface is not stable yet.

%description -l pl
Celem modu³u acpi.py jest zapewnienie jednorodnego i niezale¿nego od
platformy interfejsu do ACPI. Na t± chwilê zaimplementowane s± tylko
funkcje dotycz±ce stanu baterii. Interfejs nie jest jeszcze stabilny.

%prep
%setup -q -n %{module}.py-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CLFAGS

python %{SOURCE1} build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python %{SOURCE1} install \
        --root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE
%{py_sitedir}/*.py[co]
