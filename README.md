# BioC-JSON #

BioC-JSON is a tool that converts between BioC XML files and BioC JSON
files. BioC is a simple data structure to share text data and
annotations. More information is available at
[http://bioc.sourceforge.net](http://bioc.sourceforge.net).

When it was first implemented, XML was used for serialization. Now a
lot of data exchange occurs in JSON.  The BioC data structures have
now been implemented in JSON. The JSON structure is as similar to the
original data structures as is realistic.

In addition to its use as a comand line tool, the classes can be used
with in-memory data.

## Public Domain Notice ##

This work is a "United States Government Work" under the terms of the
United States Copyright Act. It was written as part of the authors'
official duties as a United States Government employee and thus cannot
be copyrighted within the United States. The data is freely available
to the public for use. The National Library of Medicine and the U.S.
Government have not placed any restriction on its use or reproduction.

Although all reasonable efforts have been taken to ensure the accuracy
and reliability of the data and its source code, the NLM and the
U.S. Government do not and cannot warrant the performance or results
that may be obtained by using it. The NLM and the U.S. Government
disclaim all warranties, express or implied, including warranties of
performance, merchantability or fitness for any particular purpose.

## Setup

This code uses the PyBioC library. It can be found at
[https://github.com/2mh/PyBioC](https://github.com/2mh/PyBioC). Python's `sys.path` needs to contain
the `src` directory from where PyBioC was installed. One way to do
this is to modify the `pybioc_path` line in `bioc_json.py`. Of course,
there are many other ways to do this.

The script `test_bioc_json.sh` includes some simple tests to make sure
the code is running properly on your computer.

The `json` and `xml` directories contain examples of BioC XML and BioC
JSON files.

## Usage

    ./bioc_json.py -b|-j in_file out_file

The option `-b` means convert to BioC XML, the option `-j` means convert
to BioC JSON. `in_file` and `out_file` are obvious.
