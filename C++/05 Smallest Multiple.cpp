#include <iostream>
using namespace std;

int main() {
	int t, n;
	cin >> t;
	
	do {
		cin >> n;
		int num=1;
		bool isDivisible;
		do {
			isDivisible = true;
			for (int i = 1; i <= n;i++ ) {
				if (num%i != 0) {
					isDivisible = false;
					num++;
				}

			}

			
		} while (isDivisible == false);

		cout << num << endl;

		t--;
	} while (t > 0);
	return 0;
}