#include<stdio.h>
#include<vector>
#include<stdlib.h>
#include<string.h>
using namespace std;



vector<int> visit;
vector<vector<int>> matrix;
vector<int> ans;
int max_hacked = 0;
int total = 0;

void dfs(int curr){
    if (visit[curr] == 1) return;
    visit[curr] = 1;
    for(int j=0;j<total;j++){
        if(matrix[curr][j] == 1){
            ans[curr] ++;
            dfs(j);
        }
    }
}

int main(){
    int trust_num;
    int trust, com;
    scanf("%d %d", &total, &trust_num);
    visit.assign(total+1, 0);
    matrix.assign(total+1, {});
    for(int i=0;i<total;i++) matrix[i].assign(total+1, 0);
    
    for(int i=0;i<trust_num;i++){
            scanf("%d %d", &trust, &com);
            matrix[com][trust] = 1;
    }

    for(int i=0;i<total;i++){
        
        dfs(i);
        max_hacked = ans[i] > max_hacked ? ans[i] : max_hacked;
    }

    vector<int> final;
    for(int i=0;i<total;i++){
        if(ans[i] == max_hacked) printf("%d ", ans[i]);
    }
    return 0;
}
