from typing import List


# 59 ms | 16.1 MB
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        first, second, third = m - 1, n - 1, m + n - 1
        while third >= 0:
            if second < 0 or first >= 0 and nums1[first] > nums2[second]:
                nums1[third] = nums1[first]
                first -= 1
            else:
                nums1[third] = nums2[second]
                second -= 1
            third -= 1


# 46 ms | 16.3 MB
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        first, second, third = m - 1, n - 1, m + n - 1
        while min(first, second) >= 0:
            if nums1[first] > nums2[second]:
                nums1[third] = nums1[first]
                first -= 1
            else:
                nums1[third] = nums2[second]
                second -= 1
            third -= 1
        nums, index = ((nums1, first) if first >= 0 else (nums2, second))
        while third >= 0:
            nums1[third] = nums[index]
            third -= 1
            index -= 1
