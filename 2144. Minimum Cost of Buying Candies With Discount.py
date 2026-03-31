def minimumCost(self, cost: List[int]) -> int:
    price = 0

    cost.sort(reverse=True)

    for i in range(len(cost)):
        if (i+1)%3 == 0:
            continue
        price += cost[i]
    return price