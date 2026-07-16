class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        exp=1
        for ele in nums:
            if ele<exp:
                continue
            if ele==exp:
                exp+=1
            else:
                return exp
        return exp
                

        