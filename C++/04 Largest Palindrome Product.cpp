#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isPalindrome(int input) {
	int reverse = 0;
	int n = input;
	while (input != 0) {
		reverse = (reverse * 10) + (input % 10);
		input /= 10;

	}
	if (reverse == n)
		return true;
	else return false;
}

int main() {
	int t, n;
	cin >> t;
	bool exitCond;
	for (int i = 0; i < t; i++) {
		int largestPalindrome = 0;
		cin >> n;
		for (int j = 100, exitCond = false; j < 1000 ; j++) {
			for (int k = 100; k < 1000 ; k++) {
				if (isPalindrome(j*k) == true&& j*k > largestPalindrome && j*k < n) 
					
					largestPalindrome = j*k;

				
			}

			
		}

		cout << largestPalindrome << endl;
	}
	return 0;
}
