#include <stdio.h>
int main(){
  int N;
  int x[50], y[50]; //각각 키, 몸무게
  int answer[50]; //순위 저장
  scanf("%d", &N);
  for (int i=0;i<N;i++){
    scanf("%d %d", &x[i], &y[i]);
    answer[i]=1; //모든 사람의 순위 1 로 초기화
  }
  for (int i=0;i<N;i++){
    for (int j=0;j<N;j++){
      if (x[i]<x[j] && y[i]<y[j]) //키와 몸무게가 모두 나보다 크다면
        answer[i]++; //내 순위를 1 증가시킴
    }
  printf("%d ", answer[i]);
  }
}
