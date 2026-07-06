class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res=[]
        n=min(len(strs[0]),len(strs[-1]))
        for i in range(n):
            if strs[0][i]==strs[-1][i]:
                res.append(strs[0][i])
            else: 
                break
        return "".join(res)
        