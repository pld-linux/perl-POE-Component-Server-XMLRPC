#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Component-Server-XMLRPC
Summary:	POE::Component::Server::XMLRPC - publish POE event handlers via XMLRPC over HTTP
Summary(pl.UTF-8):	POE::Component::Server::XMLRPC - procedury obsługi POE przez XMLRPC po HTTP
Name:		perl-POE-Component-Server-XMLRPC
Version:	0.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	263fd98df07331d64be5beb75b07835a
URL:		http://search.cpan.org/dist/POE-Component-Server-XMLRPC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.22
BuildRequires:	perl-POE-Component-Server-HTTP >= 0.02
BuildRequires:	perl-SOAP-Lite >= 0.28
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Server::XMLRPC adds asynchronous, event driven XMLRPC
over HTTP to your POE applications. It works very well with
synchronous XMLRPC::Lite clients, even.

%description -l pl.UTF-8
POE::Component::Server::XMLRPC dodaje asynchroniczne, sterowane
zdarzeniami XMLRPC po HTTP do aplikacji POE. Działa bardzo dobrze
nawet z synchronicznymi klientami XMLRPC::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*/*/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
