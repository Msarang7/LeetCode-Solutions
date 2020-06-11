class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        result = []

        for i in range(len(text1)+1):
        	temp = []
        	for j in range(len(text2)+1):
        		temp.append(0)
        	result.append(temp)

        #for c in result:
        #	print(c)
        #print("*"*40)

        for i in range(len(text1)):
        	for j in range(len(text2)):

        		if text1[i] == text2[j] :

        			result[i+1][j+1] = 1 + result[i][j]

        		else :

        			result[i+1][j+1] = max(result[i][j+1],result[i+1][j])

        		




        	#for c in result :
        	#	print(c)

        	#print("*"*40)


        return result[-1][-1]

text1 = "aggtab"
text2 = "gxtxayb"

obj = Solution()
obj.longestCommonSubsequence(text2,text1)

