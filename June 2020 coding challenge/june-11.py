class Solution :
    def sortColors(self, nums) :
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        curr = 0 # points to current element
        p1 = 0 # points to 1 where 0 is to be insetred if encountered. always to the left of curr or equal to curr
        p2 = len(nums)-1 
        # p2 points to extreme right initially then moves leftwards as 2's keep getting inserted at the end

        while curr <= p2 : 

        	if nums[curr] == 0 :
        		nums[curr], nums[p1] = nums[p1], nums[curr]
        		p1 = p1+1
        		curr = curr + 1
        		continue

        	if nums[curr] == 1 :
        		curr = curr + 1
        		continue

        	if nums[curr] == 2 :
        		nums[curr], nums[p2] = nums[p2], nums[curr]
        		p2 = p2 - 1

        print(nums)




inp = [2,0,2,1,1,0] 
obj = Solution()
obj.sortColors(inp)