class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            j= i+k if i+k<len(nums) else len(nums)-1
            temp=nums[i:j+1] if i+k<len(nums) else nums[i:]
            if len(set(temp))<j-i+1:
                return True
        return False

        