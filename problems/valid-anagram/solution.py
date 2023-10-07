from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(Counter(s) - Counter(t)) != 0:
            return False
        return True
