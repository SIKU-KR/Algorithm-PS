#include<iostream>
#include<string>
using namespace std;

int main() {
	string str;
	int T, i;
	cin >> T;
	for (i = 0; i < T; i++) {
		cin >> str;
		cout << str.front() << str.back() << endl;
	}
	return 0;
}