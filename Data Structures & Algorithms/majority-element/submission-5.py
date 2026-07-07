class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for ele in nums:
            if count==0:
                res=ele
            count+=1 if res==ele else -1
        return res
                
        