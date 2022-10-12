from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        if len(x) < len(nums):
            return True
        else:
            return False


a = Solution()
print(a.containsDuplicate([2, 14, 18, 22, 22]))
