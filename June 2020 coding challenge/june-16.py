class Solution:

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        # first difference between IPV4 and IPV6 is that . is used in IPV4 and : in IPV6
        
        if "." in IP:

        	numList = IP.split(".")

        	if len(numList) != 4 :
        		return "Neither"

        	for num in numList :

        		if not num.isnumeric():
        			return "Neither"

        		num_int = int(num)
        		if num_int <= 255 and num_int>=0 and num == str(num_int): 
        				continue
        		else :
        			return "Neither"
        	return "IPv4"
        	

        if ":" in IP:

        	symbols = "0123456789abcdefABCDEF" 
        	numList = IP.split(":")

        	if len(numList) != 8 :
        		return "Neither"

        	for num in numList :

        		if len(num) == 0:
        			return "Neither"

        		if len(num)>4:
        			return "Neither"

        		for ele in num:
        			if ele not in symbols:
        				return "Neither"

        	return "IPv6"

 
        else :
        	return "Neither"




obj = Solution()
a = obj.validIPAddress("2001:db8:85a3:0::8a2E:0370:7334")
print(a)