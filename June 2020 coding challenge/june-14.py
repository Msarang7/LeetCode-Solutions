class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        import math
        dist = [math.inf]*n
        dist[src] = 0

        for _ in range(k+1):
        	prev = dist[:]

        	for f in flights :
        		dist[f[1]] = min(dist[f[1]], prev[f[0]]+f[2])


        return dist[dst] if dist[dst] < math.inf else -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

obj = Solution()
ans = obj.findCheapestPrice(n,flights,src,dst,k)
print(ans)