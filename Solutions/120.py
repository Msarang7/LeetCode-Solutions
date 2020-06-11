inp = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

class Solution:
    def minimumTotal(self, triangle):
        


        result = triangle
        print(result)

        for row in range(len(triangle)-2, -1, -1):
        	for column in range(0,row+1):
        		result[row][column] = max(result[row+1][column], result[row+1][column+1]) + triangle[row][column]

        	print(result)

obj = Solution()
obj.minimumTotal(inp)