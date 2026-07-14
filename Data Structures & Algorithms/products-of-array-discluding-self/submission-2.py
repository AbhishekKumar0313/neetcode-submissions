class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=[0]*n,[0]*n
        for i in range(n):
            left[i]= nums[i] if i==0 else nums[i]*left[i-1]
            right[n-i-1]=nums[n-i-1] if n-i-1 == n-1  else right[n-i]*nums[n-i-1]
        
        res=[]
        for i in range(n):
            left_pro=left[i-1] if i>0 else 1
            right_pro=right[i+1] if i<n-1 else 1
            res.append(left_pro*right_pro)
        return res
        
        
        