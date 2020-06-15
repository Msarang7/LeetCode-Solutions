class Solution :


	# the reason to write this function is to check whether we
	# can split the input array into m subarrays such that sum of 
	# elements in every subarray is less than equal to max.

	def canSplit(self, nums, cuts, mid) :

		# nums is input array

		# cuts is number of sub arrays possible

		# mid is a value such that our goal is to find m
		# contiguous subarrays whose sum of elements is less than
		# equal to mid

		temp = 0 # stores sum of every sub array into consideration

		for num in nums :

			if num > mid :
				return False # a single element in array greater than mid is found
				# which means maximum among the sum of the subarrays will surely be more
				# than mid. So, we cannot split input array into m sub arrays such that we are able to keep
				# the maximum of sum of subarrays less than mid.

			if temp + num <= mid : 
				# num can be included in a subarray because sum 
				# of already present elements in the subarray and num is less than or equal to mid.

				temp = temp + num # sum of subarray till the element num

			else : # this else will run everytime sum of subarray becomes greater than mid.

				cuts = cuts - 1 # the value of temp+num became greater than mid hence it is one subarray
				# excluding the number num and we are decremeneting cuts by 1 because we got 1 subarray

				temp = num # for new subarray, num will be the first element in it as it couldn't be
				# added to previous subarray. Also summation will start from num, hence assiging temp = num

				if cuts < 0 :
					return False

					# " cuts < 0 " means that we have used all the number of subarrays possible without reaching
					# the end of the input array. This means value of mid parameter was smaller than required. 

					# Therefore, we need a larger value for mid. So, we will shift to the right half of the bianry tree
					# by taking left = mid + 1. right will stay the same and new value of mid will be
					# mid = (left+right)/2


		return True
		





	def splitArray(self, nums, m):



		left = max(nums) # max element of the list
		right = sum(nums) # sum of all elements of the list

		if m == 1 :
			return sum(nums)
		if m == len(nums):
			return max(nums)

		print("hi")
		while (left < right):

			mid = (right+left)/2

			if self.canSplit(nums,m-1,mid) : # m-1 is number of cuts we can make in the input array

				# if input array is able to be splitted using m-1 cuts then solution 
				# lies between left and mid. hence, right = mid for next iteration and left stays same.

				# otherwise, solution is greater than mid. Hence, left = mid + 1 and right stays same.

				right = mid

			else :

				left = mid + 1

		return int(left)
		# i don't know yet why answer will be obtained in left lmao !! 





nums = [7,2,5,10,8]
m = 2

obj = Solution()
a = obj.splitArray(nums,m)
print(a)














