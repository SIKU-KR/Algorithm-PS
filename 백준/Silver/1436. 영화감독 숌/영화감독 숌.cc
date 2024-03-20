#include "bits/stdc++.h"
using namespace std;

int main() {
    int N;
    int count = 0;
    int start = 666;
    cin >> N;
    while (true) {
        if(to_string(start).find("666") != string::npos){
            count++;
        }
        if(count == N){
            cout << start << endl;
            break;
        } else {
            start++;
        }
    }    
}