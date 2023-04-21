#include<iostream>
#include<string>
using namespace std;

int main() {
	string str;
	int index;
	cin >> str;
	cin >> index;
	cout << str[index - 1] << endl;
	return 0;
}