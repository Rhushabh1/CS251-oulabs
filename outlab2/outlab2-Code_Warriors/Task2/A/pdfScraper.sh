#!/bin/bash

wget $1 -O tempfile.pdf
pdftotext tempfile.pdf studentData.txt
rm tempfile.pdf

