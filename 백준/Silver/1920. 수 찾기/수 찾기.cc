#include "bits/stdc++.h"
using namespace std;

int main(){
    int n, m, tmp;
    cin >> n;
    vector<int> arr;
    for (int i = 0; i<n; i++){
        scanf("%d", &tmp);
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    cin >> m;
    for (int i = 0; i<m; i++){
        scanf("%d", &tmp);
        if (binary_search(arr.begin(), arr.end(), tmp))
            printf("1\n");
        else
            printf("0\n");
        }
    return 0;
}