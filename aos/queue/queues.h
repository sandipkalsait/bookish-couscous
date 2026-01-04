#include<stdbool.h>
#ifdef LINKED_LIST
#define MAX_SIZE 99

int queue[MAX_SIZE];
int rear=-1;
int front=-1;

bool isFull()
{
return front==MAX_SIZE-1 || rear==front;
}

bool isEmpty()
{
	return rear==-1;
}

void add(int value)
{
}

int remove()
{


}

#endif

