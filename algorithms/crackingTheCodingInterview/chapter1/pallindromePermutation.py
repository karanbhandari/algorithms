import sys
from collections import Counter

def pallindromePermutation(string):
	string = string.lower()
	c = Counter(string)
	single_limit_reached = False
	print(c)

	for item in c:
		if item == ' ':
			continue
		if single_limit_reached and c[item] == 1:
			return False
		elif c[item] == 1:
			single_limit_reached = True
		elif c[item] != 2:
			return False
	return True

def main():
	string = sys.argv[1]
	print(pallindromePermutation(string))

if __name__ == "__main__":
	main()