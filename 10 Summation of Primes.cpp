#include<iostream>
#include<vector>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
	int t, n;
	
	cin >> t;
	vector<bool> isPrime(2000100, true);
	
	vector<int> listOfPrimes;
	listOfPrimes.push_back(2);
	for (int i = 2; i < 2000100; i+=2) {
		if (isPrime[i] == true) {
			listOfPrimes.push_back(i + 1);
			for (int j = i + i + 1; j < 2000100 && j != 1 ; j += i + 1) {
				isPrime[j] = false;
			}
		}

	}

	do {
		cin >> n;
		unsigned long long total = 0;
		
		for (int i = 0; listOfPrimes[i] < n; i++) {
			total += listOfPrimes[i];
		}
		cout << total << endl;
		t--;
	} while (t > 0);
	return 0;
}
