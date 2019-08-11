#!/bin/bash

# awk -F, '/AA/{print $2}' $2


# awk 'BEGIN{FS=",";OFS=" ";}
# 	{if(NR>1)
# 		{	
# 			cmd="awk -F, "/$7/{print $2}" $2"
# 			system(" eval cmd ")
# 			print $5,$7;
# 		}
# 	}' $1 #> faltu.txt

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

# cat faltu.txt | while read credit grade
# do
# 	# awk -v gr=$grade '/gr/{print $2}' $2
# 	# echo $grade
# 	sed -n -e "// p" $2 | cut -d, -f2
# 	# echo $gr
# done

# rm faltu.txt
