from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for number in nums:
            if number not in d.keys():
                d[number] = 0
            d[number] += 1
        result = list(filter(lambda key: d[key] > len(nums) / 2, d.keys()))
        return result[0] if len(result) > 0 else None
