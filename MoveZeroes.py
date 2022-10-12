from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_list = [x for x in range(len(nums)) if nums[x] == 0]
        for x in range(len(zero_list) - 1, -1, -1):
            nums.pop(zero_list[x])
            nums.append(0)
        print(nums)


a = Solution()
a.moveZeroes([0, 0])
