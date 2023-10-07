from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = [[nums[0], nums[0]]]
        for num in nums[1:]:
            if num == result[-1][-1] + 1:
                result[-1][-1] = num
            else:
                result.append([num, num])
        return list(map(lambda _range: f'{_range[0]}->{_range[1]}' if _range[0] != _range[1] else str(_range[0]), result))
