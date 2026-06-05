class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # target is 0, if a > 0 then remaining values
            # (l and r) cannot add to equal 0
            if a > 0:
                break

            # skip if current a is not start, but is
            # equal to previous (duplicate)
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1

                else:
                    # append triplet
                    res.append([a, nums[l], nums[r]])
                    # move pointers
                    l += 1
                    r -= 1

                    # keep moving left if duplicate
                    # skipping left already ensures unique triplet
                    # thus no need to skip right
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
        return res