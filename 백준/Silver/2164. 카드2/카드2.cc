#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    queue<int> Q;
    for(int i = 1; i<=N; i++){
        Q.push(i);
    }
    while(Q.size() > 1){
        Q.pop();
        Q.push(Q.front());
        Q.pop();
    }
    cout << Q.front() << endl;
    // 시간초과
    // vector<int> v;
    // for (int i = 1; i<=N; i++){
    //     v.push_back(i);
    // }
    // while(v.size() != 1) {
    //     v.erase(v.begin());
    //     int tmp = v.front();
    //     v.erase(v.begin());
    //     v.push_back(tmp);
    // }
    // cout << v.front() << endl;
    return 0;
}