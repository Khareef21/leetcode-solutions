#brute force approach with O(n*m) time complexity
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        ind=-1
        max_count=-1
        for i in range(n):
            count_row=0
            for j in range(m):
                count_row+=mat[i][j]
            if count_row>max_count:
                max_count=max(max_count,count_row)
                ind=i
        return [ind,max_count]
        