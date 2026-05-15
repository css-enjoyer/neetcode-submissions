class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # resulting grouping of strings
        # defaultdict to allow initializing of missing keys
        res = defaultdict(list)

        # for each string in list of strings
        for s in strs:
            # make a counter [0,0,0,...]
            countsKey = [0] * 26

            # for each character in current string
            for c in s:
                # increment characters found in their correpsonding indices
                countsKey[ord(c) - ord("a")] += 1

            # {[0,1,0,...]: [bmw, wmb]} 
            res[tuple(countsKey)].append(s)
        
        # return as group of values, no keys
        return list(res.values())