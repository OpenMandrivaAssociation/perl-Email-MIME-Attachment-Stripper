%define module      Email-MIME-Attachment-Stripper
%define name        perl-%{module}
%define up_version  1.316
%define version     %perl_convert_version %{up_version}
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Strip the attachments from a mail
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
Requires:       perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::MIME::Modifier)
BuildRequires:  perl(MIME::Types)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Given a Email::MIME object, detach all attachments from the message. These are
then available separately.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


