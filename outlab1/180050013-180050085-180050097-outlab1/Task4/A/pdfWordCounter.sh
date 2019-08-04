#!/bin/bash

if [[ "$#" -eq 0 ]]; then
	echo "Usage: ./pdfWordCounter.sh <URL> <Word>"
	exit 1
fi

wget -q $1

filename=$( ls *.pdf )
# echo $filename

pdftotext $filename test.txt
rm $filename

echo $( grep -ciw $2 test.txt )
rm test.txt