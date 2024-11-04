#include <stdio.h>
#include <string.h>
#define MAX_SIZE 10000

int stack[MAX_SIZE];
int top = -1;

void push(int x) {
    if (top == MAX_SIZE - 1) {
        printf("stack overflow :(\n");
        return;
    }
    stack[++top] = x;
}

int pop() {
    if (top == -1) {
        return -1;
    }
    return stack[top--];
}

int size() {
    return top + 1;
}

int empty() {
    return top == -1;
}

int top_s(){
    if (top == -1){
        return -1;
    }
    return stack[top];
}


int main() {
    int N, x;
    char command[10];

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", command);
        if (strcmp(command, "push") == 0) {
            scanf("%d", &x);
            push(x);
        } else if (strcmp(command, "pop") == 0) {
            printf("%d\n", pop());
        } else if (strcmp(command, "size") == 0) {
            printf("%d\n", size());
        } else if (strcmp(command, "empty") == 0) {
            printf("%d\n", empty());
        } else if (strcmp(command, "top") == 0) {
            printf("%d\n", top_s());
        }
    }

    return 0;
}