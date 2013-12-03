%define module      Email-MIME-Attachment-Stripper
%define up_version  1.316

Name:		perl-%{module}
Version:	%perl_convert_version 1.317
Release:	1
Summary:	Strip the attachments from a mail
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Email/Email-MIME-Attachment-Stripper-1.317.tar.gz
Requires:	perl(Email::Simple::Creator)

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::MIME)
BuildRequires:	perl(Email::MIME::Modifier)
BuildRequires:	perl(MIME::Types)
BuildArch:	noarch

%description
Given a Email::MIME object, detach all attachments from the message. These are
then available separately.

%prep
%setup -q -n %{module}-%{up_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.316.0-1mdv2010.0
+ Revision: 377828
- new release
- standardized version

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.5-1mdv2009.0
+ Revision: 270895
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.31.4-3mdv2009.0
+ Revision: 256756
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.4-1mdv2008.1
+ Revision: 109610
- new version (upstream version 1.314)


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.3-1mdv2007.0
+ Revision: 111274
- fix build dependencies
- Import perl-Email-MIME-Attachment-Stripper

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.3-1mdv2007.1
- first mdv release


