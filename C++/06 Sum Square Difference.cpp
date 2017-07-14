#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int t, n;
	cin >> t;
	
	do {
		cin >> n;
		unsigned long long squareSum = 0;
		unsigned long long sumOfNum = 0;
		do {
			squareSum += pow(n, 2);
			sumOfNum += n;

			n--;
		} while (n > 0);
		cout.precision(100);
		cout <<  pow(sumOfNum, 2) - squareSum<< endl;
		t--;
	} while (t > 0);
	return 0;
}

