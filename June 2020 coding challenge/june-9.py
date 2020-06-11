class Solution :

    def isSubsequence(self, s, t):

    	if len(s) == 0 :

    		return True 

    	else :

    		index = 0 # index of string s

    		for i in range(len(t)):

    			if s[index] == t[i]:
    				index = index + 1
    			
    			if index == len(s):
    				return True

    	return False # index never reached the value equal to len(s)


obj = Solution()
print(obj.isSubsequence("axc","ahbgdc"))



        
