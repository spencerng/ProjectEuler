#include<iostream>
#include<vector>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

vector<int> stringToArray(string number) {
	vector<int> digits;
	digits.reserve(number.size());
	transform(std::begin(number), std::end(number), std::back_inserter(digits),
		[](char c) {
		return c - '0';
	}
	);

	return digits;
}

int main() {
	int testCases, numberOfDigits, consecDigits;
	string number;
	cin >> testCases;
	

	for (int i = 0; i<testCases; i++) {
		cin >> numberOfDigits >> consecDigits;
		cin >> number;
					
		unsigned long long greatestProduct = 0, product;
		
		vector<int> digits = stringToArray(number);

		for (int j = 0; j+ consecDigits-1 < numberOfDigits; j++) {
			product = 1; 
				
			for (int k = j; k < consecDigits+j; k++) {
				product *=  ((int)digits[k]);
				
			}
			if (greatestProduct < product)
				greatestProduct = product;
		}
		cout << greatestProduct << endl;
	}
	return 0;
}