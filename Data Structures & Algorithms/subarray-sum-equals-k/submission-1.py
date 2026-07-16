class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map={0:1}
        count,prefix=0,0
        for ele in nums:
            prefix+=ele
            count+=map.get(prefix-k,0)
            map[prefix]=map.get(prefix,0)+1
        return count
        