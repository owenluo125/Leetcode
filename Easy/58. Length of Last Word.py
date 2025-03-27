# https://leetcode.com/problems/length-of-last-word/submissions/1588489521/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        split = s.split(" ")
        return len(split[-1])
