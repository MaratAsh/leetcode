class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _max = 0
        chars = set()

        left = right = 0
        for right in range(len(s)):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                if left < right:
                    left += 1
            else:
                chars.add(s[right])
            _max = max(_max, right - left + 1)
        return _max
