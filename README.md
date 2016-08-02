## App::joc version 0.01
 
# DESCRIPTION

## JOC - Juniper Openconnect Client

This package provides a CLI tool to connect to Juniper VPN services using openconnect rather than the "native" Juniper client.

Different user configurations are supported by YAML files.

Tools included in this package:

  * `bin/joc`

     The Juniper Openconnect Client

  * `bin/pulse_connect`
    Shell script to connect using Juniper's `pulsesvc` client.
    Functionality is more limited than that of `joc`.

  * `bin/getx509certificate`
    Fetch the SSL certificate from a remote server and save it in PEM and DER formats.

See the POD documentation for each script.

# INSTALLATION
 
To install this software, run the following commands:

    perl Makefile.PL
    make
    make install

## Building An RPM Package

The distribution tarball comes with a `.spec` file (originally created using `cpanspec`, see this [Perl Hacks](http://perlhacks.com/2015/10/build-rpms-of-cpan-modules/) article for the finer details).

To build:

    rpmbuild -ta App-joc-0.01.tar.gz

# DEPENDENCIES
 
  * Perl Modules:
    - see `Makefile.PL`

  * Other:
	- `openconnect` v7.05 or later.
	- `openssl` (x509 and s_client)
 
# COPYRIGHT AND LICENCE
 
Copyright (C) 2016, Steven Bakker _<sb AT monkey-mind DOT net>_
 
This package is free software; you can redistribute it and/or modify
it under the same terms as Perl itself.
