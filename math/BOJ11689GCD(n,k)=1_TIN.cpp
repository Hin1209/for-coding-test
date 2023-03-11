#include <iostream> 
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;


int main(void){
    ll n;
    scanf("%llu", &n);
    vector<ll> prime;
    ll tmp = n; 
    for(ll i = 2; i * i <= n; ++i){
        if(tmp % i == 0){
            prime.push_back(i);
            while(tmp % i == 0) tmp /= i;
        }
    }
    ll res = n;
    for(int i = 0; i < prime.size(); ++i){
        res -= res / prime[i];
    }
    if(tmp > 1) res -= res / tmp;
    printf("%llu", res);
    return 0;
}
