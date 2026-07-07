class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=None,0
        for ele in nums:
            if count==0:
                res,count=ele,1
            elif ele==res:
                count+=1
            else:
                count-=1
        return res
                
        