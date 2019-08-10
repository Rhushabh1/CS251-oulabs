#!/bin/bash

awk 'BEGIN {
			OFS="|"
			FS="[:\n]"
			RS="--------------------------------------------------------------------\n\n"
			{print "Student Name", "Roll Number", "CPI", "Department", "Courses Undertaken";}
	
}
{			if ( NR > 1)
				{
				{print  $2,$4,$6,$8,$10}
				}


}' $1 > studentData.csv
