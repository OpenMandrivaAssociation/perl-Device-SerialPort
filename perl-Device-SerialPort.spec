%define upstream_name    Device-SerialPort
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/modemtest
/usr/share/man/man1/modemtest.1.lzma

