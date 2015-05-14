%define module chardet


Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	2.0.1
Release:	4.1
License:	LGPLv2+
Group:		Development/Python
Source0:	http://chardet.feedparser.org/download/python2-%{module}-%{version}.tgz
URL:		http://chardet.feedparser.org/
%py_requires -d
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%prep
%setup -q -n python2-%{module}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}

%files
%doc docs/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/%{module}
