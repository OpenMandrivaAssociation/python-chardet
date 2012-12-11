%define module	chardet
%define name	python-%{module}
%define version	2.0.1
%define rel		3
%define	release	%mkrel %rel

Summary:	Character encoding auto-detection in Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/%{module}


%changelog
* Tue Apr 24 2012 Lev Givon <lev@mandriva.org> 2.0.1-3mdv2012.0
+ Revision: 793057
- Rebuild to provide pythonegg(chardet)

* Thu Jan 28 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.1-2mdv2011.0
+ Revision: 497655
- fix license

* Thu Jan 28 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.1-1mdv2010.1
+ Revision: 497650
- bump release

* Fri May 08 2009 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 373562
- new version
- fix buildroot and URL
- use py_requires
- drop --optimize=2
- initial Mandriva release

