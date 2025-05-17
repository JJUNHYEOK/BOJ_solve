#include <stdio.h>
#define SIZE 100000

int main(){
    int arr[SIZE]; 
    int num, val;
    int cnt = 1;

    scanf("%d", &num);
    for(int i=0; i<num; i++){
        scanf("%d", &val);
        arr[i] = val;
    }

    int max = arr[num-1];


    for(int j=num-2; j>=0; j--){
        if(max<arr[j]){
            max = arr[j];
            cnt++;
        }
    }

    printf("%d", cnt);

    return 0;
}