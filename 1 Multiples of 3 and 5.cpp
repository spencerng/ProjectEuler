#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t, n;
    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> n;
        int total = 0;
        for(int j = 3; j < n; j++){
            if(j % 5 == 0 || j % 3 == 0)
                total+=j;
        }
        /*unsigned long long total = (3 * (n / 3)*((n / 3) + 1)) / 2 + (5 * (n / 5)*((n / 5) + 1)) / 2 - (15 * (n / 15)*((n / 15) + 1)) / 2;
		Optimized solution requiring math to derive
		
		*/
        cout << total << endl;
        
    }
    return 0;
}
