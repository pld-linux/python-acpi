
%define		module	acpi

Summary:	Uniform and platform independent interface to ACPI
Summary(pl):	Jednorodny i niezale¿ny od platformy interfejs do ACPI
Name:		python-%{module}
Version:	0.3.0
Release:	1
License:	Custom
Group:		Development/Languages/Python
Source0:	http://www.iapp.de/~riemer/projects/acpi.py/page.30.download/page.10.acpi.py/page.020.0.3.0/%{module}.py-%{version}-0-generic-src.tgz
# Source0-md5:	c200fc6ef00c774154ff899a0073220b
Source1:	%{name}-setup.py
URL:		http://www.iapp.de/~riemer/projects/acpi.py/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
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
%setup -q -n ACPI

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python %{SOURCE1} build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python %{SOURCE1} install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE
%{py_sitescriptdir}/*.py[co]
