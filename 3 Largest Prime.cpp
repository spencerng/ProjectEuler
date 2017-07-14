#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	long long t, n;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		int largestPrime = 1;

		do {

			if (n % 2 == 0) {
				largestPrime = 2;
				n /= 2;
			}

			else for (int j = 3; j <= n; j += 2) {
				if (n%j == 0) {
					largestPrime = j;
					n /= j;
					break;
				}

			}



		} while (n != 1);

		cout << largestPrime << endl;
	}
	return 0;
}
