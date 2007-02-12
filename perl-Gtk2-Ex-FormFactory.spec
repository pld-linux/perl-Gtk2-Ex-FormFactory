#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	Ex-FormFactory
Summary:	Gtk2::Ex::FormFactory - makes building complex GUI's easy
Summary(pl.UTF-8):	Gtk2::Ex::FormFactory - moduł ułatwiający tworzenie złożonych GUI
Name:		perl-Gtk2-Ex-FormFactory
Version:	0.65
Release:	0.1
License:	LGPL v2.1+
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

%description
This is a framework which tries to make building complex GUI's easy,
by offering these two main features:
- Consistent looking GUI without the need to code resp. tune each
  widget by hand. Instead you declare the structure of your GUI,
  connect it to the data of your program (which should be a well
  defined set of objects) and control how this structure is
  transformed into a specific layout in a very generic way.
- Automatically keep widget and object states in sync (in both
  directions), even with complex data structures with a lot of
  internal dependencies, object nesting etc.

%description -l pl.UTF-8
To jest szkielet próbujący ułatwić tworzenie złożonych GUI oferując
dwie główne cechy:
- spójnie wyglądające GUI bez potrzeby kodowania i dopasowywania
  ręcznie każdego widgetu; zamiast tego wystarczy zadeklarować
  strukturę GUI, połączyć ją z danymi programu (które powinny być
  dobrze zdefiniowanym zbiorem obiektów) i kontrolować jak ta
  struktura jest przekształcana na określony wygląd w bardzo
  ogólny sposób.
- automatyczne utrzymywanie stanu widgetów i obiektów w synchronizacji
  (w obu kierunkach), nawet dla złożonych struktur danych z dużą
  liczbą wewnętrznych zależności, zagnieżdżonymi obiektami itp.

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
install tutorial/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README{,.tutorial}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
