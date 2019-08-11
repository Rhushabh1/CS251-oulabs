awk 'BEGIN{FS=",";}
	{
		if (FNR==NR) 
			{ var[$1]=$2;
			print $1; next }
	}
	{
		if (NR!=FNR)
			{for (key in var)
				{if (key==$7) {print var[key];}
				else {print key,$7;} }
			}
	}
	END{for (key in var)
			{print key " " var[key]}}' $2 $1
