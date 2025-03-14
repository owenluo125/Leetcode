# https://leetcode.com/problems/count-symmetric-integers/submissions/1573746073/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high+1):
            x = str(x)
            number = [int(y) for y in x]
            length = len(x)
            if length % 2 == 0:
                if sum(number[length//2:]) == sum(number[:length//2]):
                    count += 1
        
        return count
