class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # creating ans array
        n=len(nums)
        ans=[0]*(2*n)
        # filling ans array
        for index,val in enumerate(nums):
            ans[index]=ans[index+n]=val
        return ans
        