class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # horizontal scanning
        n=len(strs[0])
        res=[]
        # finding minimum lenght
        for i in range(len(strs)):
            n=min(n,len(strs[i]))
        for i in range(n):
            for j in range(len(strs)):
                print(i,j)
                if strs[j]=="" or  i>=len(strs[j]) or strs[0][i]!=strs[j][i]:
                    return ''.join(res) if res!=None else ""
            res.append(strs[0][i])
        return ''.join(res) if res!=None else ""
        