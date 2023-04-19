#include<iostream>
using namespace std;

int main() {
	int N, M, a=0, b=0 ,c=0;
	cin >> N >> M;
	int* arr = new int[N]();
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> c;
		for (int j = a-1; j < b; j++) {
			arr[j] = c;
		}
	}
	for (int i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}
	delete[] arr;
	return 0;
}