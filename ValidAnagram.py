class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = [x for x in s]
        list_t = [x for x in t]
        if len(list_s) == len(list_t):
            list_s.sort()
            list_t.sort()
            for x in range(len(list_s)):
                if list_s[x] == list_t[x]:
                    continue
                else:
                    return False
            return True
        else:
            return False

s_ = "anagrat"
t_ = "nagaram"
a = Solution()
print(a.isAnagram(s=s_, t=t_))