class Solution:
    def checkAnagram(self,curr,check):
        if len(curr)!=len(check):
            return False
        array=[0]*26
        for i in range(len(curr)):
            array[ord(curr[i])-97]+=1
            array[ord(check[i])-97]-=1
        for val in array:
            if val !=0:
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        while strs:
            if len(strs)>0:
                curr=strs[0]
                temp=[]
                i=0
                while i<len(strs):
                    if self.checkAnagram(curr,strs[i]):
                        temp.append(strs[i])
                        strs.pop(i)
                        i=0
                    else:
                        i+=1
                res.append(temp)
            else:
                break
        return res




        