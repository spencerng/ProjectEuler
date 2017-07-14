#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
using namespace std;


int main() {
	vector<int> vec {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	for (int i = 1; i < 1000000; i++)
		next_permutation(begin(vec), end(vec));
	for (int i = 0; i < 10; i++)
		cout << vec[i];
	cout << endl;
	return 0;
}