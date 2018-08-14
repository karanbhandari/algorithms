#include <iostream>

using namespace std;

int main() {
	int list[5] = {4,1,2,8,7};

	// algorithm
	for (int i = 1; i < 5; i++) {
		if (list[i] < list[i - 1]) {
			int temp = list[i];
			list[i] = list [i - 1];
			list[i - 1] = temp;
		}
	}

	for (int i = 0; i < 5; i++) {
		cout << list[i] << endl;
	}
}