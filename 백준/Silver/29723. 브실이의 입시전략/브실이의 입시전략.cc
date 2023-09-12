#include<bits/stdc++.h>

using namespace std;

typedef struct grade {
	string name;
	int point;
}grade;

bool cmp(const grade& p1, const grade& p2) {
	if (p1.point < p2.point)
		return true;
	else if (p1.point < p2.point)
		return p1.name < p2.name;
	else
		return false;
}

int main() {
	int N, M, K, min, max, i, j;
	int sum = 0;

	cin >> N >> M >> K;

	grade* p = new grade[N];
	string* q = new string[K];

	for (i = 0; i < N; i++) {
		cin >> p[i].name >> p[i].point;
	}

	for (i = 0; i < K; i++) {
		cin >> q[i];
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < K; j++) {
			if (p[i].name == q[j]) {
				sum = sum + p[i].point;
				p[i].point = 0;
			}
		}
	}

	sort(p, p + N, cmp);
	max = sum;
	min = sum;

	for (i = K; i < M; i++) {
		min = min + p[i].point;
	}
	for (i = N-1; i > N - M + K - 1; i--) {
		max = max + p[i].point;
	}
	cout << min << " " << max;
	return 0;
}