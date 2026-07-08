class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start,end,move=0,len(nums)-1,0
        while move<=end:
            if nums[move]==0:
                nums[move],nums[start]=nums[start],nums[move]
                start,move=start+1,move+1
            elif nums[move]==2:
                nums[move],nums[end]=nums[end],nums[move]
                end-=1
            else:
                move+=1
        
            