#define MAX 50
#include<stdbool.h>
int Queue[MAX];
int rear=-1,front=-1;

bool isEmpty()
{
return rear==-1 || rear==front;
}

bool isFull()
{

 return rear==MAX-1;
}

void enqueue(int value)
{
 if(isFull())
 {
  printf("The queue is full");
  
 }
 else{
 Queue[++rear]=value;
// front++;
 }

}


void printQueue()
{
int start=front;
int end=rear;

printf("{");
while(start!=end)
{
printf("%d,",Queue[++start]);
}
printf("}");

}

void dequeue()
{

 if(isEmpty())
 {
	 printf("The queue is empty");
	 
 }
 else{
 int value = Queue[++front];
 printf("the removed value is %d \n",value);


 }

}


