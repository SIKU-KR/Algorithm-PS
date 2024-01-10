#include "bits/stdc++.h"
using namespace std;

int main() {
    queue<int> q;
    int n;
    string str;
    int input;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> str;
        if(str == "push"){
            cin >> input;
            q.push(input);
        } else if(str == "pop" && q.size() > 0) {
            cout << q.front() << endl;
            q.pop();
        } else if(str == "size") {
            cout << q.size() << endl;
        } else if(str == "empty") {
            if(q.empty()){
                cout << "1" << endl;
            } else {
                cout << "0" << endl;
            }
        } else if(str == "front" && q.size() > 0){
            cout << q.front() << endl;
        } else if(str == "back" && q.size() > 0){
            cout << q.back() << endl;
        } else {
            cout << "-1" << endl;
        }
    }
}