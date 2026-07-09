class Solution:
    def reverse(self,num,l,r):
        if l>=r:
            return 
        num[l],num[r]=num[r],num[l]
        self.reverse(num,l+1,r-1)

    def reverseString(self, s: List[str]) -> None:
        self.reverse(s,0,len(s)-1)