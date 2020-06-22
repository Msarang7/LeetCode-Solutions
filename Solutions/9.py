class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
        	return False


        res = []

        while(x>0):

        	res.append(x%10)
        	x = int(x/10)

        for i in range(0,int(len(res)/2)):
        	if res[i] == res[len(res)-1-i]:
        		continue
        	else :
        		return False

        return True




obj = Solution()
print(obj.isPalindrome(-121))





