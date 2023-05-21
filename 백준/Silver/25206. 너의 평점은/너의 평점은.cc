#include<iostream>
#include<string>
using namespace std;

struct Grade 
{
	string str[20];
	double credit[20];
	string grade[20];
};

double score(string grade, double credit) {
	if (grade == "A+")
		return credit * 4.5;
	else if (grade == "A0")
		return credit * 4.0;
	else if (grade == "B+")
		return credit * 3.5;
	else if (grade == "B0")
		return credit * 3.0;
	else if (grade == "C+")
		return credit * 2.5;
	else if (grade == "C0")
		return credit * 2.0;
	else if (grade == "D+")
		return credit * 1.5;
	else if (grade == "D0")
		return credit * 1.0;
	else if (grade == "F")
		return credit * 0.0;
	else
		return 0;
}

int main() {
	Grade A;
	double total = 0;
	double sumcredit = 0;
	for (int i = 0; i < 20; i++) {
		cin >> A.str[i] >> A.credit[i] >> A.grade[i];
	}
	for (int i = 0; i < 20; i++) {
		total += score(A.grade[i], A.credit[i]);
	}
	for (int i = 0; i < 20; i++) {
		if(A.grade[i] != "P")
			sumcredit += A.credit[i];
	}
	cout << total / sumcredit << endl;
	return 0;
}