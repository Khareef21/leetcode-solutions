class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n=len(dist)
        if hour<=n-1:
            return -1
        low=1
        high=10**7
        #ans= -1
        while low<=high:
            mid=low+(high-low)//2
            time=0
            for i in range(n-1):
                time+=(dist[i]+mid-1)//mid
            time+=(dist[-1]/mid)
            if time<=hour:
                # ans=mid
                high=mid-1
            else:
                low=mid+1
        return low

            

        
        