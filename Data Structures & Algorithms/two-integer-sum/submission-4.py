class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # index look up for seen
        for k,v in enumerate(nums):
            seen[v] = k
        
        for k,v in enumerate(nums):
            diff = target - v

            # if diff in seen and not the same as current
            if diff in seen and seen[diff] != k:
                return [k, seen[diff]]
        
        return []