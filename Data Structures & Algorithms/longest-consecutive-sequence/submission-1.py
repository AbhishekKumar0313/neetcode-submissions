class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count,maxlen=1,1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            elif nums[i]-nums[i-1]==1:
                count+=1
            else:
                maxlen=max(maxlen,count)
                count=1
        return max(maxlen,count)
        


        