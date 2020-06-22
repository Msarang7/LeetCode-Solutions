class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if str == "":
        	return 0

        # removing white spaces at the beginning
        if str[0] == " ":
        	while(str[0] == " "):
        		str = str[1:]
  

        strs = str.split(" ")
        #print(strs)


        # for float "3.14"



        
        if strs[0].isnumeric(): # for the case "42" and "4193 with words"
        	if int(strs[0]) > 0 :
        		if int(strs[0]) > 2**31:
        			return  2**31
        		else: 
        			return int(strs[0])

        if strs[0].startswith('-') and strs[0][1:].isdigit(): # for the case "-42"
        	if -int(strs[0][1:]) < -2**31:
        		return -2**31
        	else:
        		return -int(strs[0][1:])


        # for the case "words and 987"

        sample = "-0123456789"

        if strs[0][0] not in sample: # strs[0] contains characters then
        	return 0

        # it is float 
        return(int(float(strs[0])))









obj = Solution()
a = obj.myAtoi("")
print(a)