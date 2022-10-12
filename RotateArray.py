from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        new_array = []
        for x in range(len(nums)):
            new_array.append(0)

        if k > len(nums):
            k = k % len(nums)
        for x in range(len(nums)):
            if x + k >= len(nums):
                new_array[x + k - len(nums)] = nums[x]
            else:
                new_array[x + k] = nums[x]

        for x in range(len(nums)):
            nums[x] = new_array[x]

        print(nums)


a = Solution()
print(a.rotate([1, 2], 5))
