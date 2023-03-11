#include <iostream> 
#include <queue> 
#include <vector>

using namespace std;

char miniStar[][5] = {{' ',' ','*',' ',' '},
    {' ','*',' ','*',' '},
    {'*','*','*','*','*'}};

void printStar(int num, int y, int x, vector< vector<char> >& board);

int main(void){
    int n;
    scanf("%d", &n);
    vector< vector<char> > board(n, vector<char>(2*n-1, ' '));
    printStar(n/3, 0, 0, board);
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < 2*n-1; ++j){
            printf("%c", board[i][j]);
        }
        printf("\n");
    }

    return 0;
}

void printStar(int num, int y, int x, vector< vector<char> >& board){
    if(num == 1){
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 5; ++j){
                board[y+i][x+j] = miniStar[i][j];
            }
        }
    }
    else{
        printStar(num/2, y, x + 3 * num/2, board);
        printStar(num/2, y + 3 * num/2, x, board);
        printStar(num/2, y + 3 * num/2, x + 3 * num, board);
    }
}