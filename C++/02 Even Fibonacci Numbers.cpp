
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int testCases;
	cin >> testCases;
	
	vector<unsigned long long> fibList(93);
	vector<unsigned long long> evenFibs;
	
	fibList[0]= 1, fibList[1] = 1;
	for(int i = 2; i < 93; i++){
		fibList[i]=fibList[i-1]+fibList[i-2];
		if(fibList[i]%2==0)
			evenFibs.push_back(fibList[i]);		
	}
	
	for (int i = 0; i<testCases; i++) {
		unsigned long long total = 0;
		unsigned long long n;
		cin >> n;
		
		for(int j = 0; j < evenFibs.size()&&evenFibs[j] <= n; j++)
			total+=evenFibs[j];
					
		cout << total << endl;

	}
	return 0;
}


