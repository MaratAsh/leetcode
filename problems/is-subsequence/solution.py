class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) > len(t) or t == "":
            return False
        
        tptr, sptr = len(t) - 1, len(s) - 1
        while tptr >= 0 and sptr >= 0:
            if s[sptr] == t[tptr]:
                sptr -= 1
            tptr -= 1
        return sptr == -1
