#O(n)

import sys

def isUnique(string):
	chars = []
	for char in string:
		if char in chars:
			return False
		else:
			chars.append(char)
	return True

def main():
	print(isUnique(sys.argv[1]))

if __name__ == "__main__":
	main()