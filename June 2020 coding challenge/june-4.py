# reverse a string

inp = ["H","a","n","n","a","h"]
# output = ["h","a","n","n","a","H"]

def reverseString(str):

	n = len(str)
	for i in range(int(n/2)):
		temp = str[i]
		str[i] = str[n-i-1]
		str[n-i-1] = temp
	print(str)

reverseString(inp)