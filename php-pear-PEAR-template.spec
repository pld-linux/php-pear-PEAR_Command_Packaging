%include	/usr/lib/rpm/macros.php
%include	/usr/lib/rpm/macros.pear
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
BuildRequires:	php-pear-build
Requires:	php-pear
BuildArch:	@arch@
# @extra_headers@
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
#define		_noautoreq	'pear(XML/Beautifier/.*)'

%description
@description@

In PEAR status of this package is: %{_status}.

%description -l pl
...

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc @doc_files@
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
