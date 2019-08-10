#!/bin/bash

read text

chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

touch temp.txt
echo $text > temp.txt
# eval 'chr 65'

awk -e 'BEGIN{
		FS="";
		RS=" ";
	}
	{
		for (i=1;i<=NF;i++) 
		{
			c = eval ord $i
			$i = eval chr $(( $c+1 ))
			print $c;
		}
	}
	END{}' temp.txt