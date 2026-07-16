class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ele1,ele2,c1,c2=None,None,0,0
        for ele in nums:
            if ele==ele1:
                c1+=1
            elif ele==ele2:
                c2+=1
            elif c1==0:
                ele1,c1=ele,1
            elif c2==0:
                ele2,c2=ele,1
            else:
                c1-=1
                c2-=1
        res=[]
    
        if ele1 is not None and  nums.count(ele1)>n//3:
            res.append(ele1)
        
        if ele2 is not None and ele2 != ele1 and nums.count(ele2) > n // 3:
            res.append(ele2)
        return res

            
        