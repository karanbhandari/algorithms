#O(n)

import sys

def stringCompression(string):
	if len(string) == 0:
		return string
	result =string[0]
	i = 1
	count = 1
	while i < len(string):
		if string[i-1] == string[i]:
			count+=1
		else:
			if count == 1:
				result+=string[i]
			else:
				result+=str(count)
				count = 1
				result+=string[i]
		i+=1
		
	if count != 1:
		result+=str(count)
	return result

def main():
	print(stringCompression(sys.argv[1]))

if __name__ == "__main__":
	main()