#include <stdio.h>
#define SIZE 100000

int main(){
  int n;
  int num, cnt = 0, sum = 0;
  int stack[SIZE];

  scanf("%d", &n);

  for(int i=0; i<n; i++){
    scanf("%d", &num);
    if(num == 0)
      stack[--cnt] = 0;
    else
      stack[cnt++] = num;
  }

  for(int i=0;i<cnt;i++){
    sum += stack[i];
  }
  printf("%d", sum);

  return 0;
  
}