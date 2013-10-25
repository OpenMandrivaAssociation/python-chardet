%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	2.1.1
Release:	1
License:	LGPLv2+
Group:		Development/Python
Source:		https://pypi.python.org/packages/source/c/chardet/chardet-%{version}.tar.gz
URL:		http://chardet.feedparser.org/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}

%clean

%files
%doc docs/*
%{_bindir}/*
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}
