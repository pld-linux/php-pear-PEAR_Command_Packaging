%include	/usr/lib/rpm/macros.php
%define		_class		@class@
%define		_subclass	@subclass@
%define		_status		@release_state@
%define		_pearname	@package@

Summary:	%{_pearname} - @summary@
Summary(pl):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	@version@
Release:	1
License:	@release_license@
Group:		Development/Languages/PHP
Source0:	http://@master_server@/get/%{_pearname}-%{version}.tgz
# Source0-md5:	-
URL:		http://@master_server@/package/@package@
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
@extra_headers@
%if !@have_tests@
Obsoletes:	%{name}-tests
%endif
BuildArch:	@arch@
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if @have_optional_deps@
# exclude optional dependencies
%define		_noautoreq	@optional@
%endif

%description
@description@

In PEAR status of this package is: %{_status}.

%description -l pl
...

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%if @have_optional_deps@
%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi
%endif

%files
%defattr(644,root,root,755)
%doc install.log
%if @have_optional_deps@
%doc optional-packages.txt
%endif
@doc_files@
%{php_pear_dir}/.registry/*.reg
@files@
@data_files@

%if @have_tests@
%files tests
%defattr(644,root,root,755)
@test_files@
%endif
