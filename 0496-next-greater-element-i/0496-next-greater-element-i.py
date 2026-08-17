class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        d={}
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums2[i]:
                stack.pop()
            if len(stack)!=0:
                #your stack has already contains nums2 elements
                d[nums2[i]]=stack[-1]
            else:
                #your stack is empty
                d[nums2[i]]=-1
            stack.append(nums2[i])
        ans=[]
        for i in range(len(nums1)):
            ans.append(d[nums1[i]])
        return ans

        