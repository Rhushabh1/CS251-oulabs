#!/bin/bash

awk 'BEGIN {
			OFS="|"
			FS="[:\n]"
			RS="--------------------------------------------------------------------"
			{print "Student Name", "Roll Number", "CPI", "Department", "Courses Undertaken";}
	
}
{			if ( NF < 10)
				{}
			else
				{
				s = ""
				for( i = 12; i < NF ; i++)
				{s = s $i }
				{print  $4, $6, $8, $10, s}
				}


}' $1 > studentData.csv
