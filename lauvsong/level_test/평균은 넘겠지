#include <stdio.h>
int main(){
  int N,n; //N 은 처음 입력받는 학생 수, n 은 점수의 갯수
  int scores[1000];
  float avg;
  scanf("%d", &N);
  while (N--){
    int sum=0;
    int count=0; //입력마다 변수 재활용할것임. sum, count 초기화
    scanf("%d",&n);
    for (int i=0;i<n;i++){
      scanf("%d ", &scores[i]);
      sum+=scores[i]; //점수 합계 구함
    }
    avg = (float)sum/n; //평균 구함
    for (int i=0;i<n;i++)
      if (scores[i]>avg) count++; //점수가 평균보다 큰 경우를 셈
    printf("%.3f%%\n", (float)count*100/n); //비율 구해서 출력
  }
}
