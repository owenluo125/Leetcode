# https://leetcode.com/problems/concatenation-of-array/submissions/1480802678/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for y in range(2):
            for x in nums:
                new_list.append(x)
        return new_list
