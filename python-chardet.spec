%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	5.0.0
Release:	2
License:	LGPLv2+
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/31/a2/12c090713b3d0e141f367236d3a8bdc3e5fca0d83ff3647af4892c16c205/chardet-5.0.0.tar.gz
URL:		https://pypi.python.org/pypi/chardet
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-distribute
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE=  %{__python} setup.py install --root=%{buildroot}
mv -f %{buildroot}%{_bindir}/{,python3-}chardetect

%files
%doc docs/*
%{_bindir}/python3-chardetect
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}
