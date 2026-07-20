class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp=[0]*len(nums)
        n=len(nums)
        for i in range(n):
            temp[(i+k)%n]=nums[i]
        for i in range(n):
            nums[i]=temp[i]
        