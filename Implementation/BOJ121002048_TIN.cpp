#include <iostream> 
#include <queue> 
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int res = 0;

void moveMap(int direction, int cnt, vector< vector<int> >& world);

int main(void){
    int n, tmp;
    scanf("%d", &n);
    vector< vector<int> > world(n, vector<int>(n,0));
    vector< vector<int> > saveMap(n, vector<int>(n,0));
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            scanf("%d", &tmp);
            world[i][j] = tmp;
            saveMap[i][j] = tmp;
            if(tmp > res) res = tmp;
        }
    }
    for(int i = 1; i <= 4; ++i){
        moveMap(i, 5, world);
        for(int j = 0; j < world.size(); ++j){
            for(int k = 0; k < world.size(); ++k) world[j][k] = saveMap[j][k];
        }
    }
    printf("%d", res);

    return 0;
}


void moveMap(int direction, int cnt, vector< vector<int> >& world){
    vector< vector<int> > copyMap(world.size(), vector<int>(world.size(), 0));
    switch(direction){
        case 1:
        for(int i = 0; i < world.size(); ++i){
            for(int j = 0; j < world.size(); ++j){
                if(world[i][j] != 0){
                    int next = j + 1;
                    while(next < world.size() && world[i][next] == 0) next++;
                    if(next == world.size()) continue;
                    else if(world[i][next] == world[i][j]){
                        world[i][j] *= 2;
                        world[i][next] = 0;
                    }
                }
            }
            for(int k = 0; k < world.size(); ++k){
                if(world[i][k] == 0){
                    int next = k + 1;
                    while(next < world.size() && world[i][next] == 0) next++;
                    if(next == world.size()) continue;
                    else{
                        world[i][k] = world[i][next];
                        world[i][next] = 0;
                    }
                }
            }
        }
        break;

        case 2:
        for(int i = 0; i < world.size(); ++i){
            for(int j = world.size()-1; 0 <= j; --j){
                if(world[i][j] != 0){
                    int next = j - 1;
                    while(0 <= next && world[i][next] == 0) next--;
                    if(next == -1) continue;
                    else if(world[i][next] == world[i][j]){
                        world[i][j] *= 2;
                        world[i][next] = 0;
                    }
                }
            }
            for(int k = world.size(); 0 <= k; --k){
                if(world[i][k] == 0){
                    int next = k - 1;
                    while(0 <= next && world[i][next] == 0) next--;
                    if(next == -1) continue;
                    else{
                        world[i][k] = world[i][next];
                        world[i][next] = 0;
                    }
                }
            }
        }
        break;

        case 3:
        for(int i = 0; i < world.size(); ++i){
            for(int j = 0; j < world.size(); ++j){
                if(world[j][i] != 0){
                    int next = j + 1;
                    while(next < world.size() && world[next][i] == 0) next++;
                    if(next == world.size()) continue;
                    else if(world[next][i] == world[j][i]){
                        world[j][i] *= 2;
                        world[next][i] = 0;
                    }
                }
            }
            for(int k = 0; k < world.size(); ++k){
                if(world[k][i] == 0){
                    int next = k + 1;
                    while(next < world.size() && world[next][i] == 0) next++;
                    if(next == world.size()) continue;
                    else{
                        world[k][i] = world[next][i];
                        world[next][i] = 0;
                    }
                }
            }
        }
        break;

        case 4:
        for(int i = 0; i < world.size(); ++i){
            for(int j = world.size()-1; 0 <= j; --j){
                if(world[j][i] != 0){
                    int next = j - 1;
                    while(0 <= next && world[next][i] == 0) next--;
                    if(next == -1) continue;
                    else if(world[next][i] == world[j][i]){
                        world[j][i] *= 2;
                        world[next][i] = 0;
                    }
                }
            }
            for(int k = world.size()-1; 0 <= k; --k){
                if(world[k][i] == 0){
                    int next = k - 1;
                    while(0 <= next && world[next][i] == 0) next--;
                    if(next == -1) continue;
                    else{
                        world[k][i] = world[next][i];
                        world[next][i] = 0;
                    }
                }
            }
        }
    }
    if(cnt == 1){
        for(int i = 0; i < world.size(); ++i){
            for(int j = 0; j < world.size(); ++j){
                if(world[i][j] > res) res = world[i][j];
            }
        }
        return;
    }
    for(int i = 0; i < world.size(); ++i){
        for(int j = 0; j < world.size(); ++j) copyMap[i][j] = world[i][j];
    }
    for(int i = 1; i <= 4; ++i){
        moveMap(i, cnt-1, world);
        for(int j = 0; j < world.size(); ++j){
            for(int k = 0; k < world.size(); ++k) world[j][k] = copyMap[j][k];
        }
    }
}