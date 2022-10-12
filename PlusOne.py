from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = int("".join(str(e) for e in digits))
        sum += 1
        sum = str(sum)
        output = []
        for x in sum:
            output.append(int(x))

        return output


a = Solution()
a.plusOne([1, 2, 3])
