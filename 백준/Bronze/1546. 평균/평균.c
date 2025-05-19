#include <stdio.h>
#define SIZE 1000

int main(){
    int arr[SIZE];
    int cnt, max;
    int sum = 0;
    float avg;

    scanf("%d", &cnt);

    for(int i=0; i<cnt; i++){
        scanf("%d", &arr[i]);
    }

    max = arr[0];

    for(int j=1; j<cnt; j++){
      if(arr[j]>max){
        max = arr[j];
    }
    }

    for(int p=0; p<cnt; p++){
        sum += arr[p];
    }

    avg = (float)(sum*100)/(max*cnt);
    
    printf("%f", avg);


    return 0;
}