class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={']':'[',')':'(','}':'{'}
        for bracket in s:
            if bracket in "[{(":
                stack.append(bracket)
            else:
                if len(stack)==0 or stack[-1]!=map[bracket]:
                    return False
                stack.pop()
        return not stack



        