#!/bin/bash


sed -n -e '1 p' $1 > sortedStudentData.csv
sed -n -e '2,$ p' $1 | sort -rk3,3 -t\| -V >> sortedStudentData.csv
awk -F"|" 'NR==2,NR==6 {print $1}' sortedStudentData.csv > top5Students.txt

