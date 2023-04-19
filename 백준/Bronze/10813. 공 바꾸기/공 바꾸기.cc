#include<iostream>
using namespace std;

int main() {
	int N, M, a, b, tmp;
	cin >> N >> M;
	int* arr = new int[N]();
	for (int i = 0; i < N; i++) {
		arr[i] = i + 1;
	}
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		tmp = arr[a-1];;
		arr[a-1] = arr[b-1];
		arr[b-1] = tmp;
	}
	for (int i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}
	delete[] arr;
	return 0;
}