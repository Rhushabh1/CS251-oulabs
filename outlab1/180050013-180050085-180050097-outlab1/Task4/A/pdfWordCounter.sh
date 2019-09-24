#!/bin/bash

wget -q $1

filename=$( ls *.pdf )

echo $( pdftotext $filename - | grep -ciw $2 )

rm $filename

