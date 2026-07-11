class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        total=nums1[:m]+nums2[::]
        total.sort()
        for i in range(m+n):
            nums1[i]=total[i]
