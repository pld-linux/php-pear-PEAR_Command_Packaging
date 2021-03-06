# TODO
# - finish ../SOURCES/php-pear-PEAR-rpmvars.patch merge
# - merge conflict + upper to ">": (Mail_mimeDecode)
#   Requires:   php-pear-Mail_Mime >= 1.4.0
#   Conflicts:  php-pear-Mail_Mime = 1.4.0
#   ->
#   Requires:   php-pear-Mail_Mime > 1.4.0
# - add minimum php version used (so that the epoch does not go to nonsense for
#   older php's, yet think that could blow up php4 only pkgs)
# - if external channel not installed, channel alias can not be resolved
#   and deps get generated with full name: php-pear.docblox-project.org-DocBlox
%define		status		alpha
%define		pearname	PEAR_Command_Packaging
Summary:	%{pearname} - make-rpm-spec command for managing RPM .spec files for PEAR packages
Summary(pl.UTF-8):	%{pearname} - polecenie make-rpm-spec do zarządzania plikami .spec pakietów PEAR-a
Name:		php-pear-%{pearname}
Version:	0.3.0
Release:	0.1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://download.pear.php.net/package/%{pearname}-%{version}.tgz
# Source0-md5:	98bb036ed762c1b99d3db0e6f8a89306
Source1:	php-pear-PEAR-template.spec
Patch0:		%{name}.patch
URL:		http://pear.php.net/package/PEAR_Command_Packaging/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
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

In PEAR status of this package is: %{status}.

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

Ta klasa ma w PEAR status: %{status}.

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

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{php_pear_dir}/data/%{pearname}/template.spec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/Command/Packaging.xml
%{php_pear_dir}/PEAR/Command/Packaging.php
%{php_pear_dir}/data/PEAR_Command_Packaging
