%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	2.2.1
Release:	2
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
%setup -qn %{module}-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE=  python setup.py install --root=%{buildroot}

%files
%doc docs/*
%{_bindir}/chardetect
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}

