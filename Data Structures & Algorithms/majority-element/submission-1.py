class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for ele in nums:
            map[ele]=map.get(ele,0)+1
        n=len(nums)
        for k,v in map.items():
            if v>n//2:
                return k
        return -1
        