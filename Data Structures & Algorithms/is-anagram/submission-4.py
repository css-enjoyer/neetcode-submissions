from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}

        if (len(s) != len(t)):
            return False;

        for c in s:
            countS[c] = countS.get(c, 0) + 1

        for c in t:
            if c not in countS:
                return False
            countS[c] -= 1
            if countS[c] < 0:
                return False

        return True
        # return Counter(s) == Counter(t)