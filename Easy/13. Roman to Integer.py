# https://leetcode.com/problems/roman-to-integer/submissions/1573723514/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        temp = 0
        for x in reversed(s):
            value = roman_values[x]
            if value < temp:
                sum -= value
            else:
                sum += value
            temp = value

        return sum
