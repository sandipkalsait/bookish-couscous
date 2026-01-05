#include <stdlib.h>
#include <stdbool.h>

struct node {
    int value;
    struct node* next;
};

struct Queue {
    struct node* front;
    struct node* rear;
};

void init(struct Queue** q) {
    *q = (struct Queue*)malloc(sizeof(struct Queue));
    (*q)->front = NULL;
    (*q)->rear = NULL;
}

void enqueue(struct Queue* q, int value) {
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->value = value;
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}

int dequeue(struct Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty.\n");
        return -1;
    }
    struct node* temp = q->front;
    int dequeuedValue = temp->value;
    q->front = q->front->next;
    if (q->front == NULL) {
        q->rear = NULL;
    }
    free(temp);
    return dequeuedValue;
}

bool isEmpty(struct Queue* q) {
    return q->front == NULL;
}

void display(struct Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty.\n");
        return;
    }
    struct node* current = q->front;
    while (current != NULL) {
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");
}
