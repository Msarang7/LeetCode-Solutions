class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0 :
        	return False

        if n == 1 :
        	return True
        
        if n%2 != 0: # for odd number
        	return False


        while(True):

        	if n%2 != 0 :
        		return False

        	if n == 0 :
        		return True

        	if n == 1 :
        		return False

        	if n == 2 :
        		return True

        	n = n/2 


obj = Solution()
print(obj.isPowerOfTwo(1023))