%define module	chardet

Summary:	Character encoding auto-detection in Python
Name:		python-%{module}
Version:	2.2.1
Release:	1
License:	LGPLv2+
Group:		Development/Python
Source:		https://pypi.python.org/packages/source/c/chardet/chardet-%{version}.tar.gz
URL:		http://chardet.feedparser.org/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildArch:	noarch

%description
Character encoding auto-detection in Python. As smart as your browser.

%package -n python3-chardet
Summary:        Character encoding auto-detection in Python
Group:          Development/Python
Requires:       python3

%description -n python3-chardet
Character encoding auto-detection in Python. As smart as your browser.

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python3

%build
pushd python2
python setup.py build
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python3
PYTHONDONTWRITEBYTECODE=  %{__python3} setup.py install --root=%{buildroot}
mv %{buildroot}/%{_bindir}/chardetect.py %{buildroot}/%{_bindir}/python3-chardetect.py
popd

pushd python2
PYTHONDONTWRITEBYTECODE=  python setup.py install --root=%{buildroot}
popd

%clean

%files
%doc python2/docs/*
%{_bindir}/chardetect.py
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}

%files -n python3-chardet
%doc python3/docs/*
%{_bindir}/python3-chardetect.py
%{py3_puresitedir}/*.egg-info
%{py3_puresitedir}/%{module}
