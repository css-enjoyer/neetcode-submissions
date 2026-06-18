class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLength = 0
        
        # abcabc
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) 
            currentLength = len(charSet)
            maxLength = max(maxLength, currentLength)

        return maxLength
