class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = {}
        for x in range(len(s)):
            dict_s[s[x]] = 0
        for x in range(len(s)):
            dict_s[s[x]] += 1
        for x in range(len(s)):
            if dict_s[s[x]] == 1:
                arg = x
                return arg
        return -1


a = Solution()
print(a.firstUniqChar("loveleetcode"))
