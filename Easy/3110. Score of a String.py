# https://leetcode.com/problems/score-of-a-string/submissions/1480798073/

class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for x in range(1,len(s)):
            total += abs(ord(s[x-1]) - ord(s[x]))
        
        return total
