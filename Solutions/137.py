class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(sum(nums))
        print(sum(set(nums)))
        
        return (3 * sum(set(nums)) - sum(nums))//2


nums = [0,1,0,1,0,1,99]
obj = Solution()
a = obj.singleNumber(nums)
print(a)