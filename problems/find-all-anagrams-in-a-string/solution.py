from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        if len(s) < len(p):
            return []
        
        w_counter = defaultdict(int)
        p_counter = defaultdict(int)
        for i, ch in enumerate(p):
            p_counter[ch] += 1
            w_counter[s[i]] += 1
        
        if p_counter == w_counter:
            ans.append(0)
        w_start = 1
        w_end = len(p)
        while w_end < len(s):
            w_counter[s[w_start - 1]] -= 1
            w_counter[s[w_end]] += 1
            if w_counter[s[w_start - 1]] == 0:
                del w_counter[s[w_start - 1]]
            if w_counter == p_counter:
                ans.append(w_start)
            w_start += 1
            w_end += 1
        return ans
