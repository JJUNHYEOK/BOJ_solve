#include <stdio.h>
#define SIZE 100

int main() {
  int num;
  scanf("%d", &num);

  int line[SIZE];
  int order[SIZE];

  for (int i = 0; i < num; i++) {
    scanf("%d", &order[i]);
  }

  for (int p = 0; p < num; p++) {
    int pos = p - order[p];
    for (int j = p; j > pos; j--) {
      line[j] = line[j - 1];
    }
    line[pos] = p + 1;
  }

  for (int j = 0; j < num; j++) {
    printf("%d ", line[j]);
  }

  return 0;
}