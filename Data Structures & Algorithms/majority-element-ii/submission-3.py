class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        res=[]
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
            else:
                if count>n//3:
                    res.append(nums[i-1])
                count=1
        if count>n//3:
            res.append(nums[-1])
        return res

        