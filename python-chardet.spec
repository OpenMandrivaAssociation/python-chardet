%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	4.0.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/ee/2d/9cdc2b527e127b4c9db64b86647d567985940ac3698eeabc7ffaccb4ea61/chardet-4.0.0.tar.gz
URL:		https://pypi.python.org/pypi/chardet
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-distribute
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%package -n python2-%{module}
Summary:	Python 2 module for %{module}
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources

%description -n python2-%{module}
Python 2 module for %{module}.

%prep
%setup -qn %{module}-%{version}
cp -a . %{py2dir} 

%build
%{__python} setup.py build

pushd %{py2dir} 
%{__python2} setup.py build
popd

%install
PYTHONDONTWRITEBYTECODE=  %{__python} setup.py install --root=%{buildroot}
mv -f %{buildroot}%{_bindir}/{,python3-}chardetect

pushd %{py2dir} 
PYTHONDONTWRITEBYTECODE=  %{__python2} setup.py install --root=%{buildroot}
popd

%files
%doc docs/*
%{_bindir}/python3-chardetect
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}

%files -n python2-%{module}
%{_bindir}/chardetect
%{py2_puresitedir}/*.egg-info
%{py2_puresitedir}/%{module}
