%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	3.0.4
Release:	6
License:	LGPLv2+
Group:		Development/Python
Source0:	https://pypi.python.org/packages/source/c/chardet/chardet-%{version}.tar.gz
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
