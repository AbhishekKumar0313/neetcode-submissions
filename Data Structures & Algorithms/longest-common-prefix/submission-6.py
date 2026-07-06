class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=strs[0]
        for i in range(1,len(strs)):
            j=0
            while j<min(len(curr),len(strs[i])):
                # print(j)
                # print(i,j,strs[0][j],strs[i][j])
                if strs[0][j]!=strs[i][j]:
                    break
                j+=1
            curr=curr[:j]
            # print(curr,i,j)
        return curr