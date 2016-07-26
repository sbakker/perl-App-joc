#!/usr/bin/perl

use 5.014;
use strict;
use warnings;
use ExtUtils::MakeMaker;

my $module_name    = 'App::joc';
my $module_version = '0.01';

# List of scripts in "bin" directory.
my @scripts = qw(
    getx509certificate
    joc
    pulse_connect
);

WriteMakefile(
    NAME         => $module_name,
    VERSION      => $module_version,
    PREREQ_FATAL => 0,
    PREREQ_PM    => {
        'FindBin'         => '1.51',
        'Getopt::Long'    => '2.49',
        'IPC::Run'        => '0.94',
        'List::Util'      => '1.45',
        'NetAddr::IP'     => '4.079',
        'POSIX'           => '1.53_01',
        'Pod::Usage'      => '1.69',
        'Term::ReadKey'   => '2.33',
        'URI'             => '1.71',
        'YAML::AppConfig' => '0.19',
        'YAML::XS'        => '0.62',
        'strict'          => '1.09',
        'warnings'        => '1.34',
    },
    EXE_FILES    => [map { "bin/$_" } @scripts],
    MAN1PODS	 => { map { ("bin/$_" => "blib/man1/$_.1p") } @scripts },
    AUTHOR       => 'Steven Bakker <steven.bakker@ams-ix.net>',
);
