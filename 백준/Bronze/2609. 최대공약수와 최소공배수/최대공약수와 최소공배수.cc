#include<bits/stdc++.h>

using namespace std;

int calGCD(int N, int M) {
	if (N % M == 0)
		return M;
	else
		return calGCD(M, N % M);
}

int main() {
	int N, M;

	cin >> N >> M;

	int GCD = calGCD(N, M);
	int LCM = N * M / GCD;

	cout << GCD << endl;
	cout << LCM << endl;

	return 0;
}