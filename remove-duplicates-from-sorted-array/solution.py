from typing import List
from collections import deque

inf = float("inf")

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        deq = deque()
        last = float("-inf")
        keep_count = 0
        for i in range(len(nums)):
            if last < nums[i]:
                keep_count += 1
                last = nums[i]
                if len(deq) > 0:
                    nums[deq.popleft()] = last
                    nums[i] = inf
                    deq.append(i)
            else:
                nums[i] = inf
                deq.append(i)
        return keep_count


