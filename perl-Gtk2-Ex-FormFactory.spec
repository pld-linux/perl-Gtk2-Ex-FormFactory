#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	Ex-FormFactory
Summary:	perl(Gtk2::Ex::FormFactory) - Makes building complex GUI's easy
Name:		perl-Gtk2-Ex-FormFactory
Version:	0.65
Release:	0.1
License:	GPLv2.1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	904f6fe4b94248b56507710b29a53873
URL:		http://search.cpan.org/dist/Gtk2-Ex-FormFactory/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Gtk2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
# from pod
### Refer to http://www.exit1.org/ for
### a comprehensive online documentation.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}


%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
%{__install} tutorial/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/
mv $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README{,.tutorial}
%{__install} examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Gtk2/Ex/FormFactory.pm
%dir %{perl_vendorlib}/Gtk2/Ex/FormFactory
%{perl_vendorlib}/Gtk2/Ex/FormFactory/*pm
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%{_mandir}/man3/*
