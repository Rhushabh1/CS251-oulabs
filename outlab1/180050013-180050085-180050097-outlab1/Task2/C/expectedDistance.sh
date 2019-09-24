#!/bin/bash

k=$1


sum=0
for (( i = 0; i < $k; i++ )); do
	(( temp = $(./findTheAnswer.sh) ))
	(( sum=sum+temp ))
done
mean=$(( sum/k ))
echo $mean