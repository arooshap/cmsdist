### RPM external py2-uproot 2.9.11
## IMPORT build-with-pip

Requires: py2-numpy
%define doPython3 no
%define PipPostBuild \
   perl -p -i -e "s|^#!.*python(.*)|#!/usr/bin/env python$1|" `grep -r -e "^#\!.*python.*" %i | cut -d: -f1`
