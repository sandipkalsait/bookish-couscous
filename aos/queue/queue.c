#include<stdio.h>
#include"queuel.h"



int main()
{
    struct Queue* q;
    init(&q);

    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);

    printf("Queue after enqueuing 10, 20, 30:\n");
    display(q);

    printf("Dequeued: %d\n", dequeue(q));

    printf("Queue after dequeue:\n");
    display(q);

    if (isEmpty(q)) {
        printf("Queue is empty.\n");
    } else {
        printf("Queue is not empty.\n");
    }

    free(q);
    return 0;


}
