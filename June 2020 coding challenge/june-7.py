amount = 5
coins = [1,2,5]

class Solution:

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        table = []

        # initialization

        for row in range(len(coins)+1):
        	temp = []
        	for col in range(amount+1):
        		temp.append("s")
        	table.append(temp)
        for c in table:
        	print(c)
        print("*" * 40)
        
        # dynamic solving

        for i in range(1,amount+1): # 0 th row
        	table[0][i] = 0
        for i in range(0,len(coins)+1): # 0 th column
        	table[i][0] = 1

        for c in table:
        	print(c)

        coins.insert(0,0)

        for row in range(1,len(coins)):
        	for col in range(1,amount+1):

        		if (col - coins[row]) >= 0 :

        			table[row][col] = table[row-1][col] + table[row][col - coins[row]]
        			for c in table :
        				print(c)

        		else :

        			table[row][col] = table[row-1][col]
        			for c in table :
        				print(c)


obj = Solution()
obj.change(amount,coins)



