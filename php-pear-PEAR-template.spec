%include	/usr/lib/rpm/macros.php
%define		_class		@class@
%define		_subclass	@subclass@
%define		_status		@release_state@
%define		_pearname	@package@
Summary:	%{_pearname} - @summary@
#Summary(pl.UTF-8):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	@version@
Release:	0.1
License:	@release_license@
Group:		Development/Languages/PHP
Source0:	http://@master_server@/get/%{_pearname}-%{version}.tgz
# Source0-md5:	@tarball_md5@
URL:		http://@master_server@/package/@package@/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
@extra_headers@
BuildArch:	@arch@
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if @have_optional_deps@
# exclude optional dependencies
%define		_noautoreq	@optional@
%endif

%description
@description@

In PEAR status of this package is: %{_status}.

#%description -l pl.UTF-8
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
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
@doc_files_statement@
%{php_pear_dir}/.registry/*.reg
@files@
@data_files@

%if @have_tests@
%files tests
%defattr(644,root,root,755)
@test_files@
%endif

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: php-pear-PEAR-template.spec,v $
Revision 1.17  2007/09/03 15:00:15  adamg
- fix order

Revision 1.16  2007/09/03 00:11:45  adamg
- UTF-8 by default

Revision 1.15  2006/11/08 19:07:16  glen
- add Source0-md5 support

Revision 1.14  2006/11/08 13:23:05  glen
- no need to obsolete -tests in new packages

Revision 1.13  2006/11/08 13:22:33  glen
- no epoch defined by default

Revision 1.12  2006/04/02 13:52:09  glen
- group Development/Languages/PHP for -tests

Revision 1.11  2006/04/02 13:49:54  glen
- AutoProv: no for -tests

Revision 1.10  2006/03/07 11:16:45  glen
- BR: php-pear-PEAR

Revision 1.9  2005/11/01 13:38:03  adamg
- slash at the end of URL

Revision 1.8  2005/10/08 09:42:09  glen
- avoid creating partial -pl description / summary

Revision 1.7  2005/09/28 22:06:50  glen
- duplicate file nuked

Revision 1.6  2005/09/28 21:11:55  glen
- conditionally _noautoreq

Revision 1.5  2005/09/28 20:55:45  glen
- handle optional deps and optional tests
- handle different file classes

Revision 1.4  2005/09/28 20:40:30  glen
- handle _noautoreq and %doc files

Revision 1.3  2005/09/28 20:16:39  glen
- extra_headers are pldized now

Revision 1.2  2005/09/28 20:06:37  glen
- updated
- added tests subpackage

Revision 1.1  2005/09/18 14:05:52  glen
- based on SPECS/template-php-pear.spec
