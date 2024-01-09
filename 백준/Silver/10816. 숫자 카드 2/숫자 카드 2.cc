#include "bits/stdc++.h"
using namespace std;

int main(){
    int n, m, tmp, rst;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++){
        scanf("%d", &tmp);
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());
    cin >> m;
    for (int i = 0; i < m; i++){
        scanf("%d", &tmp);
        if(binary_search(v.begin(), v.end(), tmp)){
            rst = (upper_bound(v.begin(), v.end(), tmp) - lower_bound(v.begin(), v.end(), tmp));
            printf("%d ", rst);
        } else {
            printf("0 ");
        }
    }


}