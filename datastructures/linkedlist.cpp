#include <iostream>

class Node {
	int data;
	Node *next;

	Node(int a): data(a), next(null) {}
};


int main(int argc, char* args[]){
	for(int i = 1; i < argc; i++) {
		printf("%s\n", args[i]);
	}
	return 0;
}

