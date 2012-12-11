%define upstream_name    Device-SerialPort
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    POSIX clone of Win32::SerialPort
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Device/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides an object-based user interface essentially identical
to the one provided by the Win32::SerialPort module.

Initialization
    The primary constructor is *new* with either a _PortName_, or a
    _Configuretion File_ specified. With a _PortName_, this will open the
    port and create the object. The port is not yet ready for read/write
    access. First, the desired _parameter settings_ must be established.
    Since these are tuning constants for an underlying hardware driver in
    the Operating System, they are all checked for validity by the methods
    that set them. The *write_settings* method updates the port (and will
    return True under POSIX). Ports are opened for binary transfers. A
    separate 'binmode' is not needed.

      $PortObj = new Device::SerialPort ($PortName, $quiet, $lockfile)
           || die "Can't open $PortName: $!\n";

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man?/*
%perl_vendorlib/*
%{_bindir}/modemtest


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.40.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.40.0-3
+ Revision: 681506
- update file list
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 555795
- rebuild for perl 5.12

* Wed Dec 02 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.1
+ Revision: 472627
- import perl-Device-SerialPort


* Wed Dec 02 2009 cpan2dist 1.04-1mdv
- initial mdv release, generated with cpan2dist
