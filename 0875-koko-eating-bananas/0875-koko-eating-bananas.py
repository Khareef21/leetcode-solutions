from math import ceil

class Solution:
    def time(self, piles, speed):
        total_time = 0
        for i in range(len(piles)):
            total_time += ceil(piles[i] / speed)
        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            if self.time(piles, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low