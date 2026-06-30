class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        i=n-1
        ans=[]
        while i>=0:
            #skip spaces
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            j=i #end of the current word
            #move 'i' until it hit space
            while i>=0 and s[i]!=" ":
                i-=1
            ans.append(s[i+1:j+1])
        return " ".join(ans)
        