%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	7.6.0
Release:	1
License:	0BSD
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/c/chardet/chardet-%{version}.tar.gz
URL:		https://pypi.python.org/pypi/chardet
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch
BuildSystem:	python

%description
Character encoding auto-detection in Python. As smart as your browser.

%build -p
# The sdist is not a git checkout, so hatch-vcs needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc docs/*
%{_bindir}/chardetect
%{py_puresitedir}/*.*-info
%{py_puresitedir}/%{module}
