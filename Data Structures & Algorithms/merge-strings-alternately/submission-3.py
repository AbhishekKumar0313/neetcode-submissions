class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        p=0
        while p<len(word1) or p<len(word2):
            if p<len(word1):
                res.append(word1[p])
            if p<len(word2):
                res.append(word2[p])
            p+=1
        return ''.join(res)    
        
        