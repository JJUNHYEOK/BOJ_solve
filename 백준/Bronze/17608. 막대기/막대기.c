#include <stdio.h>

#define MAX 100000

int main() {
  int line[MAX];
  int cnt = 1;

  int len = 0;
  scanf("%d", &len);

  int data;

  for (int i = 0; i < len; i++) {
    scanf("%d", &data);
    line[i] = data;
  }

  int max_height = line[len - 1];

  for (int i = len - 2; i >= 0; i--) {
    if (line[i] > max_height) {
      cnt += 1;
      max_height = line[i];
    }
  }

  printf("%d", cnt);

  return 0;
}