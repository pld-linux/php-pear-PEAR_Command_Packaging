%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Command_Packaging
%define		_status		alpha
%define		_pearname	PEAR_Command_Packaging

Summary:	%{_pearname} - make-rpm-spec command for managing RPM .spec files for PEAR packages
Summary(pl):	%{_pearname} - polecenie make-rpm-spec do zarz�dzania plikami .spec pakiet�w PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	0.1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b78eba42122b90221c74227c70de76ad
URL:		http://pear.php.net/package/PEAR_Command_Packaging/
BuildRequires:	php-pear-PEAR
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

%description -l pl
To polecenie to ulepszona implementacja standardowego polecenia
makerpm. Zawiera kilka rozszerze� czyni�cych j� du�o bardziej
elastycznym. W przysz�o�ci mog� by� dodane podobne funkcje dla innych
zewn�trznych mechanizm�w pakiet�w.

Rozszerzone mo�liwo�ci w stosunku do oryginalnego polecenia PEAR-a
"makerpm" obejmuj�:
- mo�liwo�� definiowania pola Release z linii polece�
- bardziej zaawansowane dostosowywanie nazwy generowanego pakietu
- dodawanie wirtualnych Provides/Requires o innym formacie ni� format
  nazwy pakietu
- pr�b� inteligentnego rozr�nienia mi�dzy projektami PEAR a PECL przy
  generowaniu pakiet�w

Ta klasa ma w PEAR status: %{_status}.

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