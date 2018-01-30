Name:           perl-App-joc
Version:        0.07
Release:        1%{?dist}
Summary:        App::joc Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-joc/
Source0:        http://www.cpan.org/modules/by-module/App/App-joc-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path) >= 2.09
BuildRequires:  perl(Getopt::Long) >= 2.49
BuildRequires:  perl(IPC::Run) >= 0.94
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Socket) >= 2.013
BuildRequires:  perl(Pod::Usage) >= 1.69
BuildRequires:  perl(strict) >= 1.09
BuildRequires:  perl(Term::ReadKey) >= 2.33
BuildRequires:  perl(URI) >= 1.71
BuildRequires:  perl(warnings) >= 1.34
BuildRequires:  perl(YAML::AppConfig) >= 0.19
BuildRequires:  perl(YAML::XS) >= 0.62
Requires:       perl(File::Path) >= 2.09
Requires:       perl(Getopt::Long) >= 2.49
Requires:       perl(IPC::Run) >= 0.94
Requires:       perl(List::Util) >= 1.45
Requires:       perl(NetAddr::IP) >= 4.079
Requires:       perl(Pod::Usage) >= 1.69
Requires:       perl(strict) >= 1.09
Requires:       perl(Term::ReadKey) >= 2.33
Requires:       perl(URI) >= 1.71
Requires:       perl(warnings) >= 1.34
Requires:       perl(YAML::AppConfig) >= 0.19
Requires:       perl(YAML::XS) >= 0.62
Requires:       openconnect >= 7.05
Requires:       openssl >= 0.9.8
#Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
JOC (Juniper Openconnect Client) CLI tool

%prep
%setup -q -n App-joc-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE META.json
/usr/bin/getx509certificate
/usr/bin/joc
/usr/bin/pulse_connect
/usr/share/man/man1/getx509certificate.1p.gz
/usr/share/man/man1/joc.1p.gz
/usr/share/man/man1/pulse_connect.1p.gz

%changelog
* Mon Jan 30 2018 Steven Bakker <sb@monkey-mind.net> 0.07-1
- Release 0.07-1 (DNS lookup fixes for exlusion routes).
* Mon Jul 24 2017 Steven Bakker <sb@monkey-mind.net> 0.06-3
- Release 0.06-3 (minor DOC fixes).
* Mon May 15 2017 Steven Bakker <sb@monkey-mind.net> 0.06-1
- Release 0.06.
* Fri May  5 2017 Steven Bakker <sb@monkey-mind.net> 0.05-1
- Release 0.05.
* Mon Feb  6 2017 Steven Bakker <sb@monkey-mind.net> 0.04-1
- Release 0.04.
* Sat Feb  4 2017 Steven Bakker <sb@monkey-mind.net> 0.03-2
- Release 0.03.
* Tue Jan 17 2017 Steven Bakker <sb@monkey-mind.net> 0.02-1
- Release 0.02.
* Tue Aug 03 2016 Steven Bakker <sb@monkey-mind.net> 0.01-3
- Rebuild with POD fixes.
* Tue Aug 02 2016 Steven Bakker <sb@monkey-mind.net> 0.01-2
- Specfile fixed to include man1 and bin.
* Tue Aug 02 2016 Steven Bakker <sb@monkey-mind.net> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
