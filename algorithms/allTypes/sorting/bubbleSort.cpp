#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int list[5] = {4,1,3,9,5};

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4 - i; j++) {
			if(list[j] > list[j + 1]) {
				int temp = list[j];
				list[j] = list[j + 1];
				list[j + 1] = temp;
			}
		}
	}

	// print the resulting list
	for (int i = 0; i < 5; i++) {
		cout << list[i] << endl;
	}

}