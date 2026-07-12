class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start,move=-1,0
        while move<len(nums):
            if move==0 or nums[move]!=nums[start]:
                start+=1
                nums[start]=nums[move]
            move+=1
        return start+1
        