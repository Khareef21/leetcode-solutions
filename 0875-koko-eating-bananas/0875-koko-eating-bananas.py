from math import ceil
class Solution:
    def time(self, piles, mid):
        total_time = 0
        for i in range(len(piles)):
            total_time += ceil(piles[i] / mid)
        return total_time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_value = piles[0]
        for i in range(1, len(piles)):
            if piles[i] > max_value:
                max_value = piles[i]
        low=1
        high=max_value
        # ans=float('inf')
        while low<=high:
            mid=low+(high-low)//2
            req_time=self.time(piles,mid)
            if req_time <=h:
                # ans=mid
                high=mid-1
            else:
                low=mid+1
        # return ans
        return low 
