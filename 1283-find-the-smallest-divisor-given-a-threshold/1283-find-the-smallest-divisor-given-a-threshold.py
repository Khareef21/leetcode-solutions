# from math import ceil
class Solution:
    def possible(self,nums,mid):
        sum=0
        for i in range(len(nums)):
            # sum+=ceil(nums[i]/mid)
            sum+=(nums[i]+mid-1)//mid
        return sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.possible(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low



        