class Solution():
    

    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        people = sorted(people, key = lambda a : (-a[0],a[1]))
        print(people)
        for i in people :
            result.insert(i[1],i) # (pos,person)
        print(result)
 

inp = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

obj = Solution()
obj.reconstructQueue(inp)