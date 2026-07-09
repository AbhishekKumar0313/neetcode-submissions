class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        index=0
        while index<min(len(word1),len(word2)):
            res.append(word1[index])
            res.append(word2[index])
            index+=1
        while index<len(word1):
            res.append(word1[index])
            index+=1
        while index<len(word2):
            res.append(word2[index])
            index+=1
        return ''.join(res)
         