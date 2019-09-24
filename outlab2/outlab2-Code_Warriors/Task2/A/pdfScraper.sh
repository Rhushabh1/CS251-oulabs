#!/bin/bash

wget $1 -O tempfile.pdf
pdftotext tempfile.pdf temp.txt

rm tempfile.pdf


awk 'BEGIN {
			FS="[\n]"
			RS="--------------------------------------------------------------------\n\n"
		    print "--------------------------------------------------------------------\n";
			
}
{			
			if (NR > 1) {
				s = "" ;
				for( i = 5; i <= NF ; i++)
				{s = s $i " "; }
				{print  $1;}
				{print  $2;}
				{print  $3;}
				{print $4;}
				{print  s;}
				{print "--------------------------------------------------------------------\n";}
			}
}' temp.txt > studentData.txt

rm temp.txt