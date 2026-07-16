class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        map={}
        for ele in nums:
            map[ele]=map.get(ele,0)+1
        res=[]
        for k,v in map.items():
            if v>n//3:
                res.append(k)
        return res
        
