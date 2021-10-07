class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        container = {}
        answer = set()
        
        for num in nums:
            if(container.get(num) is None):
                container[num] = 1
            else:
                container[num] += 1
                answer.add(num)
        return list(answer)