costs = [[10,20], [30,200], [400,50], [30,20]]
print(len(costs))

def twoCitySchedCost(costs):

	n = len(costs)

	diff = [c[0] - c[1] for c in costs]
	indices = sorted(range(0,n), key = lambda k : diff[k])
	print(indices)
	total_cost = 0

	for i in range(int(n/2)):
		total_cost = total_cost + costs[indices[i]][0]
		total_cost = total_cost + costs[indices[int(n/2)+i]][1]
	print(total_cost)


twoCitySchedCost(costs)
