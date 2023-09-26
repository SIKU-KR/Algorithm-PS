#include<bits/stdc++.h>

using namespace std;

int arr[8];

int checkAscending() {
	for (int i = 1; i < 7; i++) {
		if (arr[i] > arr[i + 1]) {
			return -1;
		}
	}
	return 1;
}

int checkDscending() {
	for (int i = 1; i < 7; i++) {
		if (arr[i] < arr[i + 1]) {
			return -1;
		}
	}
	return 1;
}

int main() {
	int key;
	for (int i = 0; i < 8; i++) {
		cin >> arr[i];
	}
	if (arr[0] < arr[1]) { /* check assending */
		key = checkAscending();
		if (key == 1)
			cout << "ascending" << endl;
		else
			cout << "mixed" << endl;
	}
	else { /* check descending */
		key = checkDscending();
		if (key == 1)
			cout << "descending" << endl;
		else
			cout << "mixed" << endl;
	}
	return 0;
}