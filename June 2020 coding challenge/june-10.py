class Solution :
    def searchInsert(self, nums, target) :
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i in range(0,len(nums)):
            
            if nums[i] == target :
                return i
            else :
                if nums[i] > target :
                    return i

        return i+1 # when number to be inseted is greater than every number in the list


nums = [1,3,5,6]
target = 5

obj = Solution()
print(obj.searchInsert(nums,target))