class Solution:
    def possible(self, weights, mid):
        days = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] <= mid:
                load += weights[i]
            else:
                days += 1
                load = weights[i]
        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
        
        