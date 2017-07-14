#include<iostream>
#include<vector>
#include <string>
#include <cmath>
using namespace std;

//use the idea that Pythagoream Triples can be constructed with any
//m and n, where a = n^2-m^2, b = 2mn, c=n^2+m^2

int main() {
	int testCases, num;

	cin >> testCases;	

	for (int i = 0; i<testCases; i++) {
		cin >> num;
		int greatestTriple = -1;
		for(int m=2; m < num; m++){
			for(int n = 2; n < num; n++){
				if(2*n*(n+m)==num&&2*m*n*(pow(n, 4)-pow(m, 4))>greatestTriple)
					greatestTriple=2*m*n*(pow(n, 4)-pow(m, 4));
				
			}
			
		}
		cout << greatestTriple << endl;
	}
	return 0;
}