class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            no_digits=0
            temp=nums[i]
            while temp>0:
                no_digits+=1
                temp //=10     #removes last digit
            if no_digits % 2 == 0:
                count+=1
        return count


        