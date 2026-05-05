class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for k, v in enumerate(nums):
            seen[v] = k

        for k, v in enumerate(nums):
            diff = target - v
            if diff in seen and seen[diff] != k:
                return [k, seen[diff]]
        return []

        
        