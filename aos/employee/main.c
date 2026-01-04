#include<stdio.h>
#include<string.h>
struct Employee{
int empId;
char name[30];
float salary;
};
void display(struct Employee* employee);

void displayArray(struct Employee employee[],int size)
{
	
	for(int i=0;i<size;i++)
	{
	  display(&employee[i]);
	}
  
}
void display(struct Employee* employee)
{
	
	printf("\nEmployee Id: %d , Name : %s , Salary : %f \n",employee->empId,employee->name,employee->salary);
}

int main(int argc,char** argv)
{
	struct Employee employeeFirst,employeeA[2],*employeeP,employeeLast;
	employeeFirst.empId=101;
	strcpy(employeeFirst.name,"Sandip.Kalsait\0");
	employeeFirst.salary=5000000.0;
	printf("\nwith simple display\n");
	display(&employeeFirst);

	employeeA[0].empId=101;
        strcpy(employeeA[0].name,"Sandip.Kalsait\0");
        employeeA[0].salary=5000000.0;
	//display(employeeA[0]);

	employeeA[1].empId=102;
        strcpy(employeeA[1].name,"Kajal.Kalsait\0");
        employeeA[1].salary=9000000.0;
        //display(employeeArray[1]);
	printf("\nwith array display\n");
	displayArray(employeeA,2);

	employeeP=employeeA;
	
	printf("\nWith Pointer display");
	display(employeeP);
	employeeP++;
	display(employeeP);

	for(int i=0;i<argc;i++)
	{
		printf("cmd : %d : %s \n",i,argv[i]);
	}
	if(argc==4)
	{
		 employeeLast.empId=atoi(argv[1]);
                 strcpy(employeeLast.name,argv[2]);
                 employeeLast.salary=atof(argv[3]);
	}
	display(&employeeLast);
	
	

	return 1;
}
