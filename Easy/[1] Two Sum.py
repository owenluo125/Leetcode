# https://leetcode.com/problems/two-sum/submissions/1599080684/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] + nums[y] == target:
                    return [x, y]
