#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
using ll = long long;
int dy[2]={1,0},dx[2]={0,1};
int k,n,m,world[101][101][2];
ll path[101][101];
ll solve(int y,int x){
    if(y==n&&x==m) return 1;
    ll& ret = path[y][x];
    if(ret!=-1) return ret;
    ret = 0;
    for(int i=0;i<2;i++){
        if(!world[y][x][i]){
            int ny=y+dy[i],nx=x+dx[i];
            if(ny<=n&&nx<=m) ret+=solve(ny,nx);
        }
    }
    return ret;
}
int main(){
    scanf("%d%d%d",&n,&m,&k);
    while(k--){
        int y1,x1,y2,x2;
        scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
        if(y1>y2)swap(y1,y2);
        else if(x1>x2)swap(x1,x2);
        if(y1<y2) world[y1][x1][0]=1;
        else if(x1<x2) world[y1][x1][1]=1;
    }
    memset(path,-1,sizeof(path));
    printf("%lld",solve(0,0));
}