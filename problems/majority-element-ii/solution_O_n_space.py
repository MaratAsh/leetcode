from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        c_nums = Counter(nums)
        limit = len(nums) / 3
        for num, count in c_nums.items():
            if count > limit:
                ans.append(num)
        return ans
