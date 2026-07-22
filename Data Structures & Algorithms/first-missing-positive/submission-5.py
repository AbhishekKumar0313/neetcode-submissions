class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            if nums[index]>0 and nums[index]<=len(nums) and nums[nums[index]-1]!=nums[index]:
                nums[nums[index]-1],nums[index]=nums[index],nums[nums[index]-1]
            else:
                index+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1        

        