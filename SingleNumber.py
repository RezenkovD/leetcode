from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        el = []
        nums.sort()
        for x in range(len(nums) - 1):
            if nums[x] == nums[x + 1]:
                el.append(nums[x])
        el = set(el)
        nums = set(nums)
        nums -= el
        a = list(nums)
        return a[0]


a = Solution()

print(a.singleNumber([4, 1, 2, 1, 2]))
