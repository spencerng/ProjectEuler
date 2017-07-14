#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int t, n;
	cin >> t;
	vector<int> listOfPrimes;
	listOfPrimes.push_back(2);
	listOfPrimes.push_back(3);
	do {
		cin >> n;
		unsigned int size = listOfPrimes.size();
		for (int i = listOfPrimes[size - 1]+2; n > listOfPrimes.size(); i+=2) {
			bool isPrime = true;

			for (unsigned int j = 1; j < size && isPrime==true; j++) {
				if (i % listOfPrimes[j] == 0)
					isPrime = false;
			}
			if (isPrime == true) {
				listOfPrimes.push_back(i);
				size = listOfPrimes.size();
			}
		}
		cout << listOfPrimes[n - 1] << endl;
		t--;
	} while (t > 0);
	return 0;
}

