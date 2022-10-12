from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = [s[x] for x in range(len(s) - 1, -1, -1)]
        print(a)


a = Solution()
a.reverseString(["h", "e", "l", "l", "o"])
