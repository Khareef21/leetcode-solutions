class Solution:
    def possible(self, bloomDay, day, m, k):
        flowers = 0
        bouquets = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
            else:
                bouquets += flowers // k
                flowers = 0
        bouquets += flowers // k
        if bouquets >= m:
            return True
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(bloomDay, mid, m, k)==True:
                high = mid - 1
            else:
                low = mid + 1
        return low