#include <stdio.h>

int main(){
    int a1, a0, c, n0;

    scanf("%d %d", &a1, &a0);
    scanf("%d", &c);
    scanf("%d", &n0);

    int rst = 1;

    if(c<a1){
        rst = 0;
    }
    
    if((c-a1)*n0<a0){
        rst = 0;
    }

    printf("%d\n", rst);

    return 0;


}