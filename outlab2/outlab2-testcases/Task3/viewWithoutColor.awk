BEGIN{
	FS=",";
	x=0;
}
{	
	if(NR==1){
	for( j = 0; j < 17*NF; ++j ){
	printf "-";}
	printf "\n";
	for( i=1; i<=NF; ++i ){
	if($i!="Name"){
	 printf("%20s",$i) ;}
	 else{
	 x=i;}
	}
	printf"\n";
	for( j = 0; j < 17*NF; ++j ){
	printf "-";}}
	else 
{
	for( k=1; k<=NF; ++k ){
	if(k!=x){
	printf("%20s",$k);
	}
	}
}
printf "\n";}
	
END{
	
}