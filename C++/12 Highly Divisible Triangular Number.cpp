#include<iostream>
#include<vector>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
	int t, n;
	
	cin >> t;
	vector<int> triNumbs;
	triNumbs.push_back(1);

	do {
		cin >> n;
		
		int factors = 1;
		int lastAdded=1;
		for(int i = 1; factors <= n; i+=lastAdded+1){
			lastAdded++;
			for(int j =2; j <=i; j++){
				if(i%j==0)
					factors++;
				
			}
			if(factors >n)
				cout << i << endl;
			else factors = 1;
			
		}
		
		t--;
	} while (t > 0);
	return 0;
}
