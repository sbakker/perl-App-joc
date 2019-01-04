## App::joc version 0.10
 
## DESCRIPTION

### JOC - Juniper Openconnect Client

This package provides a CLI tool to connect to PulseSecure VPN services (formerly Juniper VPN) using openconnect rather than the "native" Pulse client.

Different user configurations are supported by YAML files.

Tools included in this package:

  * `bin/joc`

     The Juniper Openconnect Client

  * `bin/pulse_connect`

    Shell script to connect using the "native" `pulsesvc` client.
    Functionality is more limited than that of `joc`.

  * `bin/getx509certificate`

    Fetch the SSL certificate from a remote server and save it in PEM and DER formats.

See the POD documentation for each script.

## INSTALLATION
 
To install this software, run the following commands (probably best as `root`):

    perl Makefile.PL
    make
    make install

### Building An RPM Package

The distribution tarball comes with a `.spec` file (originally created using `cpanspec`, see this [Perl Hacks](http://perlhacks.com/2015/10/build-rpms-of-cpan-modules/) article for the finer details).

To build:

    rpmbuild -ta App-joc-0.10.tar.gz

## DEPENDENCIES
 
  * Perl Modules:
    - see `Makefile.PL`

  * Other:
	- `openconnect` v7.05 or later.
	- `openssl` (x509 and s_client)
 
## COPYRIGHT AND LICENCE
 
Copyright (c) 2016, Steven Bakker _<sbakker AT cpan.org>_
 
This package is free software; you can redistribute it and/or modify
it under the same terms as Perl itself.
