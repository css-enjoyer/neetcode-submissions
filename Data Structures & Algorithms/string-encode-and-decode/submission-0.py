class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # for each string in array
        for s in strs:
            # append "6#string"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # ex res: 4#leet4#code
        # loop over string
        while i < len(s):
            j = i
            # while j is at number
            while s[j] != "#":
                # move j to delimiter
                j += 1
            # take length (i is at start, j at delimiter)
            length = int(s[i:j])

            # append result
            # "j+1" is just out of delimiter (first character)
            # "j+1+length" is integer of next string (before last character)
            res.append(s[j + 1 : j + 1 + length])

            # move i to next word (integer of next string)
            i = j + 1 + length
        return res
