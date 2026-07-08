class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter=[0]*3
        for v in nums:
            counter[v]+=1
        index=0
        for i in range(3):
            count=counter[i]
            while count:
                nums[index]=i
                count-=1
                index+=1
            
        

        