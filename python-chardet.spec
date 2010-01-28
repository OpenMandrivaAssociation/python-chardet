
%define module	chardet
%define name	python-%{module}
%define oname	chardet
%define version	2.0.1
%define rel	1

Summary:	Character encoding auto-detection in Python
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	LGPLv2.1+
Group:		Development/Python
Source:		http://chardet.feedparser.org/download/python2-%{module}-%{version}.tgz
URL:		http://chardet.feedparser.org/
BuildRoot:	%{_tmppath}/%{name}-root
%py_requires -d
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%prep
%setup -q -n python2-%{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install \
	--root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/%{module}
