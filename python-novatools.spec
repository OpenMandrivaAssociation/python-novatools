%define module novatools
Name:           python-%module
Version:        2.0
Release:        2
License:        BSD
Summary:        Client library for OpenStack Nova API
Url:            https://pypi.python.org/pypi/python-%module
Group:          Development/Python
Source:         python-%module-2.0.tar.gz
BuildRequires:  python-devel python-setuptools python-sphinx
Requires:       python-prettytable python-httplib2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildarch:	noarch

%description
A client for the OpenStack Nova API. There's a Python API
(the novatools module), and a command-line script (novatools).
Each implements 100% of the OpenStack Nova API.

%prep
%setup -q

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}
make -C docs html
rm docs/_build/html/.buildinfo

%files 
%defattr(-,root,root)
%doc docs/_build/html
%doc README.rst
%{_bindir}/%module
%{python_sitearch}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 2.0-1mdv2011.0
+ Revision: 683260
- import python-novatools


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 2.0
- first release for Mandriva 

