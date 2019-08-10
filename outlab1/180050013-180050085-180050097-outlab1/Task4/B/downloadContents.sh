#!/bin/bash

wget -r -q -P $2 $1 -np -k

tree -a -J -o urlReport.json

echo $( md5sum urlReport.json )

result=$( grep -c '{' urlReport.json )
echo $result


resultnew=$( ps -p $result --format cmd )


if [[ "$?" -eq 1 ]]; then
	echo No such process
else
	echo $resultnew
fi