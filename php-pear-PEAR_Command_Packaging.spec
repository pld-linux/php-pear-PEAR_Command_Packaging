# TODO
# - finish ../SOURCES/php-pear-PEAR-rpmvars.patch merge
%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	PEAR_Command_Packaging
Summary:	%{_pearname} - make-rpm-spec command for managing RPM .spec files for PEAR packages
Summary(pl.UTF-8):	%{_pearname} - polecenie make-rpm-spec do zarządzania plikami .spec pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	4
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	457881b46b8c42ba58cdb698872df2e6
Source1:	php-pear-PEAR-template.spec
Patch0:		php-pear-PEAR_Command_Packaging.patch
URL:		http://pear.php.net/package/PEAR_Command_Packaging/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.3
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
- Allows virtual Provides/Requires that differ in format from the
  package name format
- tries to intelligently distinguish between PEAR and PECL when
  generating packages

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
To polecenie to ulepszona implementacja standardowego polecenia
makerpm. Zawiera kilka rozszerzeń czyniących ją dużo bardziej
elastycznym. W przyszłości mogą być dodane podobne funkcje dla innych
zewnętrznych mechanizmów pakietów.

Rozszerzone możliwości w stosunku do oryginalnego polecenia PEAR-a
"makerpm" obejmują:
- możliwość definiowania pola Release z linii poleceń
- bardziej zaawansowane dostosowywanie nazwy generowanego pakietu
- dodawanie wirtualnych Provides/Requires o innym formacie niż format
  nazwy pakietu
- próbę inteligentnego rozróżnienia między projektami PEAR a PECL przy
  generowaniu pakietów

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

rm docs/PEAR_Command_Packaging/LICENSE

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

sed -e '/^\$''Log: /,$d' %{SOURCE1} > $RPM_BUILD_ROOT%{php_pear_dir}/data/%{_pearname}/template.spec
echo '$''Log: $' >> $RPM_BUILD_ROOT%{php_pear_dir}/data/%{_pearname}/template.spec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/Command/Packaging.xml
%{php_pear_dir}/PEAR/Command/Packaging.php
%{php_pear_dir}/data/PEAR_Command_Packaging
