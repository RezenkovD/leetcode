from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for x in range(len(prices) - 1):
            if prices[x] < prices[x + 1]:
                sum += prices[x + 1] - prices[x]
            else:
                continue
        return sum


a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
