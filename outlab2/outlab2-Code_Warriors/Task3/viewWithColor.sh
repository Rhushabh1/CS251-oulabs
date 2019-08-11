#!/bin/bash

source defineColors.sh

# printf $RED_FONT 
# printf $BLACK_BACKGROUND
# echo "this is black"

awk 'NR>3{print $6 }' $1 > abcd.txt 

sed -n -e '1,3 p' $1

x=4
NC='\033[0m'
cat abcd.txt | while read line
do 

	font=$( sed -n -e "/$line/ p" $2 | cut -d, -f3 )
	background=$( sed -n -e "/$line/ p" $2 | cut -d, -f4 )
	# echo $font $background
	f="_FONT"
	b="_BACKGROUND"
	font="printf \$$font$f"
	background="printf \$$background$b"
	# echo $font$background
	eval $font
	eval $background
	sed -n "$x p" $1 
	tput sgr0 ; 
	
	# printf $NC
	# printf $RESET_ALL
	# echo $(tput sgr0)
	(( x++ ))

done

rm -r abcd.txt


