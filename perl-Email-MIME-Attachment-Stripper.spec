%define module      Email-MIME-Attachment-Stripper
%define upstream_version  1.317

Name:		perl-%{module}
Version:	%perl_convert_version 1.317
Release:	3
Summary:	Strip the attachments from a mail
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Email/Email-MIME-Attachment-Stripper-1.317.tar.gz
Requires:	perl(Email::Simple::Creator)

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::MIME)
BuildRequires:	perl(Email::MIME::Modifier)
BuildRequires:	perl(MIME::Types)
BuildRequires:  perl(Capture::Tiny)
BuildArch:	noarch

%description
Given a Email::MIME object, detach all attachments from the message. These are
then available separately.

%prep
%setup -q -n %{module}-%{upstream_version} 

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

