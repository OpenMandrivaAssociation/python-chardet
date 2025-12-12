%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	5.2.0
Release:	2
License:	LGPLv2+
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/c/chardet/chardet-%{version}.tar.gz
URL:		https://pypi.python.org/pypi/chardet
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-distribute
BuildArch:	noarch
BuildSystem:	python

%description
Character encoding auto-detection in Python. As smart as your browser.

%files
%doc docs/*
%{_bindir}/chardetect
%{py_puresitedir}/*.*-info
%{py_puresitedir}/%{module}
