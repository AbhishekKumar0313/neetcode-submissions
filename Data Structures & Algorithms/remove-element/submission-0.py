class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr,move=0,0
        while move<len(nums):
            if nums[move]!=val:
                nums[move],nums[curr]=nums[curr],nums[move]
                curr+=1
            move+=1
        return curr
        