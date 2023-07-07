#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
	int T;
	char tmp;
	char right = ')';
	char left = '(';
	cin >> T;

	for (int i = 0; i < T; i++) {
		queue<char> q;
		string str;
		int count = 0;
		cin >> str;
		for (int j = 0; j < str.length(); j++) {
			q.push(static_cast<char>(str[j]));
		}

		if (q.front() == right) {
			cout << "NO" << endl;
			continue;
		}

		while (!q.empty() && count >= 0) {
			tmp = q.front();
			q.pop();
			if (tmp == right)
				count--;
			else if (tmp == left)
				count++;
			else
				break;
		}

		if (count == 0)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;

	}
	return 0;
}