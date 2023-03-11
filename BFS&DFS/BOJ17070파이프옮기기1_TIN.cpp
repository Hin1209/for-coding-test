#include <iostream> 
#include <queue> 
#include <vector>

using namespace std;

int main(void){
    int n;    
    scanf("%d", &n);
    vector< vector<int> > world(n,vector<int>(n,0));
    for(int i=0; i < n; ++i){
        for(int j=0; j < n; ++j){
            int tmp;
            scanf("%d ", &tmp);
            if(tmp == 1) world[i][j] = 1;
        }
    }
    int status = 0;
    int x = 1;
    int y = 0;

    queue<int> st;
    queue<int> posx;
    queue<int> posy;

    st.push(status);
    posx.push(x);
    posy.push(y);

    int count = 0;

    while(!st.empty()){
        status = st.front();
        x = posx.front();
        y = posy.front();
        st.pop();
        posx.pop();
        posy.pop();
        if(y == n-1 && x == n-1){
            ++count;
            continue;
        }
        if(status == 0){
            if(x+1 < n && world[y][x+1] == 0){
                st.push(0);
                posy.push(y);
                posx.push(x+1);
            }
            if(x+1 < n && y+1 < n && world[y][x+1] == 0 && world[y+1][x] == 0 && world[y+1][x+1] == 0){
                st.push(2);
                posy.push(y+1);
                posx.push(x+1);
            } 
        }
        else if(status == 1){
            if(y+1 < n && world[y+1][x] == 0){
                st.push(1);
                posx.push(x);
                posy.push(y+1);
            }
            if(x+1 < n && y+1 < n && world[y][x+1] == 0 && world[y+1][x] == 0 && world[y+1][x+1] == 0){
                st.push(2);
                posy.push(y+1);
                posx.push(x+1);
            }
        }
        else if(status == 2){
            if(y+1 < n && world[y+1][x] == 0){
                st.push(1);
                posx.push(x);
                posy.push(y+1);
            }
            if(x+1 < n && y+1 < n && world[y][x+1] == 0 && world[y+1][x] == 0 && world[y+1][x+1] == 0){
                st.push(2);
                posy.push(y+1);
                posx.push(x+1);
            }
            if(x+1 < n && world[y][x+1] == 0){
                st.push(0);
                posy.push(y);
                posx.push(x+1);
            }
        }
    }
    printf("%d", count);
    return 0;
}