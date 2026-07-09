class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkpal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return checkpal(l,r-1) or checkpal(l+1,r)
            l,r=l+1,r-1
        return True