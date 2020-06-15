class Solution:
    def largestDivisibleSubset(self, nums):

    	if len(nums) == 0 : 
    		return []

    	ans = [[num] for num in nums]

    	nums.sort()

    	for i in range(len(nums)):

    		for j in range(i): # for all the smaller numebrs encountered before in the list

    			if nums[i] % nums[j] == 0 and len(ans[i]) < len(ans[j])+1:
    				# why len(ans[i]) < len(ans[j])+1 ?????????
    				ans[i] = ans[j] + [nums[i]]

    	print(ans)

    	return max(ans, key = len)





nums = [4,5,8,12,16,20]

obj = Solution()
ans = obj.largestDivisibleSubset(nums)
print(ans)










