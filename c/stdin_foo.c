#include <stdio.h>
#include <stdlib.h>

int main() {

  char buf[100];
  read(0, buf, 100);

  if (buf[0] == 'f') {
    printf("one\n");
    if (buf[1] == 'o') {
      printf("two\n");
      if (buf[2] == 'o') {
        printf("three\n");
        if (buf[3] == '!') {
          printf("four\n");
          abort();
        }
      }
    }
  }

}