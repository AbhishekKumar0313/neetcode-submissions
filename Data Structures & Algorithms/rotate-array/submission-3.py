class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def helper(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left,right=left+1,right-1
        n=len(nums)
        k=k%n
        helper(0,n-k-1)
        helper(n-k,n-1)
        helper(0,n-1)