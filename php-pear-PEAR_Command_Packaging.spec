%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Command_Packaging
%define		_status		alpha
%define		_pearname	PEAR_Command_Packaging

Summary:	%{_pearname} - make-rpm-spec command for managing RPM .spec files for PEAR packages
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	0.1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	59d0355c3d0ce9ed558462f08daaa63a
URL:		http://pear.php.net/package/PEAR_Command_Packaging/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This command is an improved implementation of the standard makerpm
command, and contains several enhancements that make it far more
flexible. Similar functions for other external packaging mechanisms
may be added at a later date.

Enhanced features over the original PEAR "makerpm" command include:
- Ability to define a release on the command line
- Allows more advanced customisation of the generated package name
- Allows virtual Provides/Requires that differ in format from the package name
  format
- tries to intelligently distinguish between PEAR and PECL when generating
  packages

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/Command/Packaging.xml
%{php_pear_dir}/PEAR/Command/Packaging.php
%{php_pear_dir}/data/PEAR_Command_Packaging
