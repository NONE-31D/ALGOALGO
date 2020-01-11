#include <stdio.h>
int main(){
    int n;
    int num;
    int nums[10001] = {0};
    
    scanf("%d", &n);
    
    for (int i=0;i<n;i++){
        scanf("%d", &num);
        nums[num]++;
    }
    
    for (int i=0;i<=10000;i++){
        for (int j=0;j<nums[i];j++)
            printf("%d\n", i);
    }
}
