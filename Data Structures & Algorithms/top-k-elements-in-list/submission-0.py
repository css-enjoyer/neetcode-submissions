from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKNums = defaultdict(int) # dict of num: count pairs

        # scan nums, increment each num count
        for num in nums:
            topKNums[num] += 1

        # sort topKNums by value, reverse
        topKNums = sorted(topKNums.items(), key=lambda item: item[1], reverse=True)
        
        return [key for key, value in topKNums[:k]]