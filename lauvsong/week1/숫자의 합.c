#include <stdio.h>
int main() {
  int n;
  scanf("%d ", &n);
  int sum = 0;
  while (n--) {
    char c;
    scanf("%c", &c);
    sum += c - 48; // 공백 없이 입력하므로 문자 형태로 받을 수 밖에 없음, 0 을 뜻하는 48 만큼을 빼줌
  }
  printf("%d\n", sum);
  return 0;
}
