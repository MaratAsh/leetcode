from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_ctr = Counter(s1)
        s2_ctr = defaultdict(int)
        for i in range(len(s1)):
            s2_ctr[s2[i]] += 1
        if s2_ctr == s1_ctr:
            return True
        for start, end in zip(range(1, len(s2) - len(s1) + 1), range(len(s1), len(s2))):
            s2_ctr[s2[end]] += 1
            s2_ctr[s2[start - 1]] -= 1
            if s2_ctr[s2[start - 1]] <= 0:
                del s2_ctr[s2[start - 1]]
            if s2_ctr == s1_ctr:
                return True
        return False


print(Solution().checkInclusion('ab', 'eidbaooo'))
print(Solution().checkInclusion('ab', 'eidboaoo'))
print(Solution().checkInclusion('adc', 'dcda'))
