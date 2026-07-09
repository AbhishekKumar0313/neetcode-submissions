class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=[]
        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                string.append(ch.lower())
        return string==string[::-1]
        