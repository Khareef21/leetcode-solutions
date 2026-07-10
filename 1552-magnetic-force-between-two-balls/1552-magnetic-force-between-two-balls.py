class Solution:
    def canWePlace(self,position,mid,m):
        count_balls=1
        pos_balls=position[0]
        for i in range(1,len(position)):
            if position[i]-pos_balls>=mid:
                count_balls+=1
                pos_balls=position[i]
        return count_balls>=m
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low=1
        high=position[-1]-position[0]
        # ans=0
        while low<=high:
            mid=low+(high-low)//2
            if self.canWePlace(position,mid,m)==True:
                # ans=mid
                low=mid+1
            else:
                high=mid-1
        return high
                
        