class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map={}
        n=len(nums)
        for i in range(n):
            if nums[i] in map and i-map[nums[i]]<=k:
                return True
            map[nums[i]]=i
        return False
            