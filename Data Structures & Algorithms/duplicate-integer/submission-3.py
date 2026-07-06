class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=set()
        for ele in nums:
            if ele in check:
                return True
            check.add(ele)
        return False