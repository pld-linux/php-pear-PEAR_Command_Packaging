# TODO
# - finish ../SOURCES/php-pear-PEAR-rpmvars.patch merge
%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Command_Packaging
%define		_status		alpha
%define		_pearname	PEAR_Command_Packaging
%include	%{_sourcedir}/php-pear-build-macros
Summary:	%{_pearname} - make-rpm-spec command for managing RPM .spec files for PEAR packages
Summary(pl):	%{_pearname} - polecenie make-rpm-spec do zarz±dzania plikami .spec pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	0.10
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b8b3e3791c687e8ddaaeac7c65732233
Source1:	php-pear-PEAR-template.spec
Patch0:		php-pear-PEAR_Command_Packaging.patch
URL:		http://pear.php.net/package/PEAR_Command_Packaging/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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
- Allows virtual Provides/Requires that differ in format from the
  package name format
- tries to intelligently distinguish between PEAR and PECL when
  generating packages

In PEAR status of this package is: %{_status}.

%description -l pl
To polecenie to ulepszona implementacja standardowego polecenia
makerpm. Zawiera kilka rozszerzeñ czyni±cych j± du¿o bardziej
elastycznym. W przysz³o¶ci mog± byæ dodane podobne funkcje dla innych
zewnêtrznych mechanizmów pakietów.

Rozszerzone mo¿liwo¶ci w stosunku do oryginalnego polecenia PEAR-a
"makerpm" obejmuj±:
- mo¿liwo¶æ definiowania pola Release z linii poleceñ
- bardziej zaawansowane dostosowywanie nazwy generowanego pakietu
- dodawanie wirtualnych Provides/Requires o innym formacie ni¿ format
  nazwy pakietu
- próbê inteligentnego rozró¿nienia miêdzy projektami PEAR a PECL przy
  generowaniu pakietów

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0

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
