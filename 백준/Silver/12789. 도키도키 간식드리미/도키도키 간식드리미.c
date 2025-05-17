#include <stdio.h>
#define SIZE 1000000

int main(){
    int top = -1;
    int num, val;
    int now[SIZE];
    int spc[SIZE];
    int idx = 0; int current = 1;

    scanf("%d", &num);
    for(int i=0; i<num; i++){
        scanf("%d", &now[i]);
    }

    while(idx < num){
        if(now[idx] == current){
            current++;
            idx++;
        }
        else if(top != -1 && spc[top] == current){
            top--;
            current++;
        }
        else{
            spc[++top] = now[idx++];
        }
    }

    while(top != -1 && spc[top] == current){
        top--;
        current++;
    }

    if(top == -1){
        printf("Nice\n");
    }
    else{
        printf("Sad\n");
    }

    return 0;
}