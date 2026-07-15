class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hashset=set(nums)
        res=1
        for val in hashset:
            if val-1 in hashset:
                continue
            curr=val
            length=1
            while curr+1 in hashset:
                curr+=1
                length+=1
            res=max(res,length)
        return res