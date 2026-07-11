class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        total=nums1[:m]+nums2[::]
        nums1[::]=sorted(total)[::]