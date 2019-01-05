#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;
	return;
}

int main() {
	// sample array of integers
	int list[5] = {4,2,7,10,2};

	for (int i = 0; i < 5; i++) {
		int smallestSoFar = i;
		int j = i;
		while (j < 5) {
			if (list[smallestSoFar] > list[j]) {
				smallestSoFar = j;
			}
			j++;
		}
		swap(list[i],list[smallestSoFar]);	
	}

	for (int i = 0; i < 5; i++) {
		cout << list[i] << endl;
	}
	return 0;
}