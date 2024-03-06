#include "bits/stdc++.h"
using namespace std;

int result[41] = { -1, };
int rcount[41] = { 0, };


int main() {
    for (int i = 0; i <= 40; i++){
        if(i == 0 || i == 1) {
            result[i] = i;
            rcount[i] = 1;
        } else {
            result[i] = result[i-1] + result[i-2];
            rcount[i] = rcount[i-1] + rcount[i-2];
        }
    }

    int T, N;
    cin >> T;
    for (int i = 0; i < T; i++){
        cin >> N;
        cout << rcount[N]-result[N] << " " << result[N] << endl;
    }
    return 0;
}