class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict alows initializing missing keys, so we don't need a guard
        res = defaultdict(list)

        for s in strs: # for each string in the string list
            # we build a character count list
            count = [0] * 26

            for c in s: # for each character in the string
                # we increment that character
                count[ord(c) - ord("a")] += 1

            # append character count list with value string in result
            # use tuple because keys must be immutable
            res[tuple(count)].append(s)
        
        return list(res.values())
