#!/bin/bash


cat $1 | grep -w $3  | grep -w $4 | awk -F, '{print $0}' > aaa.txt

awk 'BEGIN{FS=",";
			RS="\r\n";
			creditcount=0;
			actualcount=0;}
	{FS=",";
		if (FNR>1 && FNR==NR ) 
			{ var[$1]=$2; }
	}
	{FS=",";
		if (FNR>1 && NR!=FNR )
			{creditcount+=$5 * var[$7];
			actualcount+=$5; }
	}
	END{cpi=creditcount/actualcount;
		printf "%0.4f\n",cpi}' $2 aaa.txt

rm -r aaa.txt

