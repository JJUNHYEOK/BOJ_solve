#include <stdio.h>
#include <stdlib.h>

int main(){

    char a, b, c, d, e, f;
    scanf("%c%c%c %c%c%c", &a, &b, &c, &d, &e, &f);

    char arr1[4] = {c,b,a};
    char arr2[4] = {f,e,d};

    int num1 = atoi(arr1);
    int num2 = atoi(arr2);

    if(num1>num2){
        printf("%d", num1);
    }

    else printf("%d", num2);


    return 0;
    



}