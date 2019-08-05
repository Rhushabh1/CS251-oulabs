#!/bin/bash

OLDIFS=$IFS
IFS=","

while read team stu1 roll1 stu2 roll2 stu3 roll3 
do
	
		echo "$team,$stu1,$roll1" >> $2
		echo "$team,$stu2,$roll2" >> $2
		echo "$team,$stu3,$roll3" >> $2


done < $1



