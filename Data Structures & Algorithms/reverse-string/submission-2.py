class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack=[]
        for ele in s:
            stack.append(ele)
        for i in range(len(s)):
            s[i]=stack.pop()
        