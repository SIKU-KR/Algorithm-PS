#include "bits/stdc++.h"
using namespace std;

int main() {
    deque<int> dq;
    int n, input;
    string str;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> str;
        if(str == "push_front") {
            cin >> input;
            dq.push_front(input);
        } else if (str == "push_back") {
            cin >> input;
            dq.push_back(input);
        } else if (str == "pop_front" && dq.size() > 0) {
            cout << dq.front() << endl;
            dq.pop_front();
        } else if (str == "pop_back" && dq.size() > 0) {
            cout << dq.back() << endl;
            dq.pop_back();
        } else if (str == "size") {
            cout << dq.size() << endl;
        } else if (str == "empty") {
            if(dq.empty()){
                cout << "1" << endl;
            } else {
                cout << "0" << endl;
            }
        } else if (str == "front" && dq.size() > 0) {
            cout << dq.front() << endl;
        } else if (str == "back" && dq.size() > 0) {
            cout << dq.back() << endl;
        } else {
            cout << "-1" << endl;
        }
    } 
}