# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for jewel in range(len(jewels)):
            for stone in range(len(stones)):
                if jewels[jewel] == stones[stone]:
                    count += 1
        return count
