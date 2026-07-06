class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map=defaultdict(list)
        for i in range(len(nums)):
            map[nums[i]].append(i)
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            total=nums[i]+nums[j]
            if total==target:
                if nums[i]==nums[j]:
                    return [min(map[nums[i]][0],map[nums[i]][1]),max(map[nums[i]][0],map[nums[i]][1])]
                return [min(map[nums[i]][0],map[target-nums[i]][0]),max(map[nums[i]][0],map[target-nums[i]][0])]
            elif total>target:
                j-=1
            else:
                i+=1
        return [-1,-1]
