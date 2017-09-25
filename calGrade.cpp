#include <iostream>

using namespace std;

int main() {
	int xf = 0;
	double jd = 0.0;
	int total = 0;
	double grade = 0.0;
	int count = 100;
	while (cin >> xf >> jd) {
		total += xf;
		grade += xf * jd;
		cout << "total is " << total << " grade is " << grade << endl; 
	}
	cout << grade / total << endl;
	return 0;
}
