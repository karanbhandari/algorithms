import sys
from collections import Counter

def oneEditInsert(string1, string2):
	len1 = len(string1)
	len2 = len(string2)
	cannot_modify_anymore = False

	i = 0
	j = 0
	while j < len2:
		if i == len2-1 and not cannot_modify_anymore:	
			return True
		elif i == len2-1 and cannot_modify_anymore:
			return False

		if string1[i] != string2[j] and not cannot_modify_anymore:
			cannot_modify_anymore = True
			j+=1
			continue
		elif string1[i] != string2[j] and cannot_modify_anymore:
			return False
		i+=1
		j+=1
	return True


def oneEditReplace(string1, string2): 
	len1 = len(string1)
	len2 = len(string2)

	cannot_modify_anymore = False

	i = 0
	j = 0

	while i < len1 and j < len2:
		if(string1[i] != string2[j] and not cannot_modify_anymore):
			cannot_modify_anymore = True
			j+=1
			i+=1
			continue
		elif string1[i] != string2[j] and cannot_modify_anymore:
			return False
		j+=1
		i+=1
	return True


def oneAway(string1, string2):
	if string1 == string2:
		return True

	# if string1 is shorter -> we can only add one character
	if(len(string1) < len(string2)):
		return oneEditInsert(string1, string2)

	# if string 2 is shorter -> we can only add one character
	elif len(string1) > len(string2):
		return oneEditInsert(string2, string1)

	# if string 1 and string2 are same length -> we can only replace one character
	elif len(string2) == len(string1):
		return oneEditReplace(string1, string2)


def main():
	s1 = sys.argv[1]
	s2 = sys.argv[2]

	print(oneAway(s1, s2))

if __name__ == "__main__":
	main()