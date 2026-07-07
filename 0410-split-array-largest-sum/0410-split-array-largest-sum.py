class Solution:
    def largestSum(self,nums,mid):
        sub_array=1
        sub_array_sum=0
        for i in range(len(nums)):
            if sub_array_sum+nums[i]<=mid:
                sub_array_sum+=nums[i]
            else:
                sub_array+=1
                sub_array_sum=nums[i]
        return sub_array
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.largestSum(nums,mid)<=k:
                high=mid-1
            else:
                low=mid+1
        return low
        