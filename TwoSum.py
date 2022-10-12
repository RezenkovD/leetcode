from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_out = []
        count_1 = 0
        count_2 = 0
        sort_nums = sorted(nums)
        while True:
            if (
                int(sort_nums[count_1] + sort_nums[len(sort_nums) - 1 - count_2])
                == target
            ):
                values_out.append(sort_nums[count_1])
                values_out.append(sort_nums[len(sort_nums) - 1 - count_2])
                break
            else:
                if (
                    sort_nums[count_1] + sort_nums[len(sort_nums) - 1 - count_2]
                    > target
                ):
                    count_2 += 1
                    continue
                else:
                    count_1 += 1
                    continue
        output = []
        for x in range(len(nums)):
            if nums[x] == values_out[0] or nums[x] == values_out[1]:
                output.append(x)

        return output


a = Solution()
print(a.twoSum([-10, -1, -18, -19], -19))
