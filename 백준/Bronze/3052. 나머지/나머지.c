#include <stdio.h>
#define SIZE 10

int main(){
    int cnt = 0;
    int input;
    int rst[SIZE];

    for(int i=0; i<SIZE; i++){
        scanf("%d", &input);
        rst[i] = input%42;
    }

    for(int j=0; j<SIZE; j++){
        int k;
        for(k=0; k<j; k++){
            if(rst[j] == rst[k]){
                break;
            }
        }

        if(j == k){
            cnt++;
        }
    }

 
    printf("%d", cnt);


    return 0;


}