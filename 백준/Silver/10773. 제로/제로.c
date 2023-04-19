#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

struct Stack {
	int top;
	int capacity;
	int* array;
};

struct stack* CreateStack(int cap) {
    struct Stack* S = malloc(sizeof(struct Stack));
    if (!S)
        return NULL;
    S->capacity = cap;
    S->top = -1;
    S->array = malloc(S->capacity * sizeof(int));
    if (!S->array)
        return NULL;
    return S;
}

void push(struct Stack* s, int data) {
    s->array[++s->top] = data;
    return;
}

int pop(struct Stack* s) {
    return(s->array[s->top--]);
}

int main() {
    int k, data, sum=0;
    scanf("%d", &k);
    struct Stack* MyStack = CreateStack(k);
    for (int i = 0; i < k; i++) {
        scanf("%d", &data);
        if (data == 0)
            pop(MyStack);
        else
            push(MyStack, data);
    }
    while (MyStack->top != -1)
        sum += pop(MyStack);
    printf("%d", sum);
    return 0;
}