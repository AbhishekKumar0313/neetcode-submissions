class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for index,val in enumerate(nums):
            rem=target-val
            if rem in map:
                return [map[rem],index]
            map[val]=index
        return [-1,-1]
