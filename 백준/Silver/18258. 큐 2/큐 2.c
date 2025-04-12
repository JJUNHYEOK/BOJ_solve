#include <stdio.h>
#include <string.h>

int main() {
  int cnt;
  int queue[2000001] = {0};
  int front = -1;
  int rear = -1;
  char cmd[10];
  int p;

  scanf("%d", &cnt);

  for (int i = 0; i < cnt; i++) {
    scanf("%s", cmd);

    if (strcmp(cmd, "push") == 0) {
      scanf("%d", &p);
      queue[++rear] = p;
    }

    if (strcmp(cmd, "pop") == 0) {
      if (rear == front)
        printf("-1\n");
      else
        printf("%d\n", queue[++front]);
    }

    if (strcmp(cmd, "size") == 0) {
      printf("%d\n", rear - front);
    }

    if (strcmp(cmd, "empty") == 0) {
      if (rear == front)
        printf("1\n");
      else
        printf("0\n");
    }

    if (strcmp(cmd, "front") == 0) {
      if (rear == front)
        printf("-1\n");
      else
        printf("%d\n", queue[front + 1]);
    }

    if (strcmp(cmd, "back") == 0) {
      if (rear == front)
        printf("-1\n");
      else
        printf("%d\n", queue[rear]);
    }
  }

  return 0;
}
