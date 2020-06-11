# not done yet

import random

class Solution:

	def __init__(self, w):

		self.w = w
		self.sums = []
		self.sums.append(self.w[0]-1)


		sum = 0
		for i in range(1,len(w)):
			sum = sum + w[i]
			self.sums.append(sum)


	def pickIndex(self):

		target = random.randint(0,self.sums[-1])
		print("target is : " + str(target))

		for c in self.sums:
			if c > target :
				print(self.sums.index(c))
				return self.sums.index(c)

w = [3,14,1,7] 
obj = Solution(w)
obj.pickIndex()

# part 2







