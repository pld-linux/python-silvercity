# TODO
# cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
Summary:	SilverCity is a lexing package, based on Scintilla
Name:		python-silvercity
Version:	0.9.7
Release:	1
License:	BSD
Group:		Development/Languages/Python
URL:		http://silvercity.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/silvercity/Python%20SilverCity%20Bindings/%{version}/SilverCity-%{version}.tar.gz
# Source0-md5:	4ae4f9691798385dbde3df9cbb228e8c
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SilverCity is a lexing package, based on Scintilla, that can provide
lexical analysis for over 20 programming and markup langauges.
SilverCity can be used as a C++ library and also has scripting
language bindings for Python.

%prep
%setup -q -n SilverCity-%{version}
%{__sed} -i -e "1i#!%{_bindir}/env python" PySilverCity/Scripts/*.py

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT{%{_bindir}/*.py,%{_examplesdir}/%{name}-%{version}}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if "%{py_ver}" > "2.4"
%{py_sitedir}/SilverCity-*.egg-info
%endif
%attr(755,root,root) %{py_sitedir}/SilverCity/_SilverCity.so
%{py_sitedir}/SilverCity/*.py[co]
%{py_sitedir}/SilverCity/default.css
%{_examplesdir}/%{name}-%{version}
