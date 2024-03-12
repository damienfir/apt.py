apt.py
======

A wrapper for `apt` for more convenient searching and installing packages.

```
> apt.py curl
.
.
.
18: libcurl-ocaml - OCaml curl bindings (Runtime Library)
17: libflickcurl0 - C library for accessing the Flickr API
16: flickcurl-doc - utilities to call the Flickr API from command line
15: libcurlpp-dev - c++ wrapper for libcurl (development files)
14: r-cran-rcurl - GNU R General network (HTTP/FTP/...) client interface
13: lua-curl-dev - libcURL development files for the Lua language
12: libcurl4-doc - documentation for libcurl
11: libcurl3-nss - easy-to-use client-side URL transfer library (NSS flavour)
10: r-cran-curl - GNU R modern and flexible web client for R
9: php8.2-curl - CURL module for PHP
8: slang-curl - transfer files using HTTP and FTP from S-Lang
7: libcurlpp0 - c++ wrapper for libcurl
6: php-curl - CURL module for PHP [default]
5: lua-curl - libcURL bindings for the Lua language
4: libcurl4 - easy-to-use client-side URL transfer library (OpenSSL flavour)
3: tclcurl - Tcl bindings to libcurl
2: s3curl - Easily interact with AWS S3 HTTP services
1: curl - command line tool for transferring data with URL syntax
Packages to install: 1
.
.
.
```

Building
--------

```
make
```

The executable will be in the `dist` folder.
