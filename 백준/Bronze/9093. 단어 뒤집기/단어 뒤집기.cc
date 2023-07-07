#include <iostream>
#include <string>
#include <sstream>
#include <deque>
#include <algorithm>
using namespace std;

int main() {
	
	int T;
	cin >> T;
	cin.ignore();

	for (int i = 0; i < T; i++) {
		string str1, word;
		getline(cin, str1);

		//문자열을 스트림화
		stringstream ss(str1);

		//덱에 저장
		deque<string> dq;

		//공백으로 분리해서 저장
		while (getline(ss, word, ' ')) {
			dq.push_back(word);
		}
		
		//하나씩 꺼내서 뒤집으며 출력
		while (!dq.empty()) {
			word = dq.front();
			dq.pop_front();
			reverse(word.begin(), word.end());
			cout << word << ' ';
		}
	}
	return 0;
}