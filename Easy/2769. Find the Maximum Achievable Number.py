# https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return 2*t + num
