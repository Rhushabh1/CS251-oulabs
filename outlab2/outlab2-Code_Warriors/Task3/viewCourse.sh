#!/bin/bash

sed -n -e '1,3 p' $1

x=$1

awk '{print $3," ",$4 }' $1 | grep -n $2 | awk -F: '{print $1}' > temp.txt 

# for i in temp.txt 
# do
# 	echo $i
# 	awk 'NR=="$i"{print $0}' "$x" 
# done

cat temp.txt | while read i
do
	sed -n "$i p" $x
done
rm -r temp.txt