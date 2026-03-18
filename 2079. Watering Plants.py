# water n plants in your garden with a watering can. 
# The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i. 
# There is a river at x = -1 that you can refill your watering can at.

# simulation: key is that it takes 2*i + 1 steps to refill from the river and water plant i.

def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        og_capacity = capacity

        for i in range(len(plants)):
            if capacity - plants[i] >= 0:
                steps += 1
                capacity -= plants[i]
            else:
                steps += (2*i +1)
                capacity = og_capacity
                capacity -= plants[i]
        return steps

# O(n) time and O(1) space