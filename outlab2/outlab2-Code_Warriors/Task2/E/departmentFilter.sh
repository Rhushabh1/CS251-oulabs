#!/bin/bash

var=$( ls $1 )

for file in $var
do
var1=$( awk -F ":" '/Department/ { print $2 }' "$file" )


if [[ -d "$var1" ]]; 
then
	cp $1/$file "$var1"
else
	mkdir "$var1" 
	cp $1/$file "$var1"

fi

done
