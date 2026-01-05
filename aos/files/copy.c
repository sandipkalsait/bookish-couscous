#include<stdio.h>
#include<stdlib.h>

long fsize(FILE *fp)
{
	long size;
	if(fp==NULL)
	{
	return -1;
	}
	fseek(fp,0,SEEK_END);
	size=ftell(fp);
	rewind(fp);

	return size;
}

int main(int argc,char* argv[])
{
FILE *fp1,*fp2;
char data[100];

if(argc==3)
{
	fp1=fopen(argv[1],"r");
	fp2=fopen(argv[2],"w");

	if(fp1==NULL || fp2==NULL)
	{
	printf("\nError in opening files");
	return 0;
	}

//	printf("\nfile1 : %s",argv[1]);
//	printf("\nfile2 : %s\n",argv[2]);
	
	while((fgets(data,sizeof(data),fp1))!=NULL)
	{
		fputs(data,fp2);
		
	}
	if(fsize(fp1)==fsize(fp2))
	{
		printf("File successsfully copied !\n");
		printf("From %s to %s \n",argv[1],argv[2]);
	}
	fclose(fp1);
	fclose(fp2);
}
else
{
printf("\nplease provide required arguments\n");
}
return 0;
}

