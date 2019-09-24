#!/bin/bash


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
		printf "%0.4f\n",cpi}' $2 $1

