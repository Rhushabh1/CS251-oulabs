#!/bin/bash

#sort -t'|' -k3  studentData.csv > sortedStudentData.csv

awk 'NR<2{ print $0;next}{print $0| "sort -t\| -n -k3 " }' studentData.csv > sortedStudentData.csv

awk 'NR==2,NR==6 {print $1}' sortedStudentData.csv > top5Students.txt

