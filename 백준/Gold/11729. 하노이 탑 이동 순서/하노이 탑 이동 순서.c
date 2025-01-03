#include <stdio.h>
#include <math.h>

void hanoi_tower(int n, char from, char tmp, char to)
{
    if(n==1){ 
    printf("%c %c\n",from,to);
    return;
    }
    else{
        hanoi_tower(n-1,from,to,tmp);
        printf("%c %c\n",from,to);
        hanoi_tower(n-1,tmp,from,to);
       
    }


}

int main()
{
    int input;
    scanf("%d",&input);

    if (input > 20){
        return 0;
    }
    long long int count = pow(2,input)-1;
    printf("%lld\n",count);
    hanoi_tower(input,'1','2','3');
    return 0;
}