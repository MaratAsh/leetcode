from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        last = nums[1]
        lastcnt = 1 + (1 if nums[1] == nums[0] else 0)
        index = 2
        for i in range(2, len(nums)):
            if last < nums[i]:
                last = nums[i]
                nums[index] = nums[i]
                index += 1
                lastcnt = 0
            elif lastcnt < 2:
                nums[index] = nums[i]
                index += 1
            else:
                nums[i] = float("inf")
            lastcnt += 1
        return index
