#include<stdio.h>
#include<stdlib.h>
#define BUFFER_SIZE 256

int main(int argc,char** argv)
{
FILE *fp;
//static char buffer[BUFFER_SIZE];
int ch;
//ideal for use of EOF in case of ASCII
int ch_counter=0;
if(argc==2)
{

	
	fp=fopen(argv[1],"r");
	if(fp==NULL)
	{
		printf("Please provide valid file name\n");
		return 0;

	}
	//while((fgets(buffer,sizeof(buffer),fp))!=NULL)
	while( ( ch = fgetc(fp) ) != EOF)
	{
		//printf("%c",ch);
		ch_counter++;

		//printf("%s",buffer);
	}
	fclose(fp);

	printf("\nFile is read successfully !");
	printf("\nCharacters count in file %s is =>  %d \n",argv[1],ch_counter);

}

else{
	printf("Please provide valid argument\n");
}

return 1;
}
