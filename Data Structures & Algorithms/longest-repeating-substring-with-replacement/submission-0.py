class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # character count map
        count = {}
        
        maxLength = 0
        l = 0

        for r in range(len(s)):
            # set count of s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # while windowLength - mostFrequentWithinWindow > allowedReplacements
            # windowLength - mostFrequentWIthinWindow = numberOfNeededReplacements
            # if numberOfNeededReplacements > allowedReplacements
            #     we shrink the window from the left and update character count
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            # maxLength vs currentWindowLength
            maxLength = max(maxLength, r - l + 1)

        return maxLength

                