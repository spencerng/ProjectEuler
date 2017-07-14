#include<iostream>
#include<vector>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
	int grid[20][20];
	for(int i = 0; i < 20; i++){
		for(int j = 0; j < 20; j++){
			cin >> grid[i][j];
		}
		
	}
	unsigned long long product;
	unsigned long long greatestProduct=0;
	//horizontal
	for(int i = 0; i < 20; i++ ){
		for(int j = 3; j < 20; j++){
			product= grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3];
			if(product > greatestProduct)
				greatestProduct=product;
		}
		
	}
	//vertical
	for(int i = 3; i < 20; i++ ){
		for(int j = 0; j < 20; j++){
			product= grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j];
			if(product > greatestProduct)
				greatestProduct=product;
		}
		
	}
	//diagonal down to right
	for(int i = 3; i < 20; i++ ){
		for(int j = 3; j < 20; j++){
			product= grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3];
			if(product > greatestProduct)
				greatestProduct=product;
		}
		
	}
	//diagonal down to left
	for(int i = 3; i < 20; i++ ){
		for(int j = 3; j < 20; j++){
			product= grid[i][j-3]*grid[i-1][j-2]*grid[i-2][j-1]*grid[i-3][j];
			if(product > greatestProduct)
				greatestProduct=product;
		}
		
	}
	cout << greatestProduct << endl;
	return 0;
}
