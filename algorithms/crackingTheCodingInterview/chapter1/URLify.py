import sys

def urlify(string, number):
	result = []
	for i in range(int(number)):
		if string[i] == " ":
			result.append("%20")
		else:
			result.append(string[i])

	answer = ""
	for i in range(len(result)):
		answer +=result[i]

	return answer

def main():
	string = sys.argv[1]
	number = sys.argv[2]
	print(urlify(string, number))

if __name__ == "__main__":
	main()