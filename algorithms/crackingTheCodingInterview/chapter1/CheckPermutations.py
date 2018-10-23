from collections import Counter
import sys

def checkPermutations(string1, string2):
	if len(string1) != len(string2):
		return False

	s1 = Counter(string1)
	s2 = Counter(string2)

		# print(s1, s2)

	for item in s1:
		if s1[item] != s2[item]:
			return False
	return True

def main():
	print(checkPermutations(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
	main()