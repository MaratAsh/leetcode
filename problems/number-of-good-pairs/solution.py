from typing import List
from math import factorial
from collections import Counter



def C_n_k(n: int, k: int):
    return factorial(n) // (factorial(k) * factorial(n - k))


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for num, count in Counter(nums).items():
            if count == 2:
                res += 1
            elif count > 1:
                res += C_n_k(count, 2)
        return res
