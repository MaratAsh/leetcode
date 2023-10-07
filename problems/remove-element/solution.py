from typing import List
from collections import deque

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        deq = deque()
        equal = 0
        for i in range(len(nums)):
            if nums[i] == val:
                deq.append(i)
                nums[i] = float("inf")
                equal += 1
            elif len(deq) > 0:
                swap_index = deq.popleft()
                nums[swap_index] = nums[i]
                nums[i] = float("inf")
                deq.append(i)
        return len(nums) - equal


