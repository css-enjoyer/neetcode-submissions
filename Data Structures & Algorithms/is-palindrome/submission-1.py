import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Skip over non alpha numeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            # Return false on any mismatch
            if s[l].lower() != s[r].lower():
                return False

            # Move left right pointers
            l += 1
            r -= 1
            
        return True;
            