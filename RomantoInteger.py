import re


class Solution:
    def romanToInt(self, s: str) -> int:

        pattern = [
            "IV",
            "IX",
            "XL",
            "XC",
            "CD",
            "CM",
            "I",
            "V",
            "X",
            "L",
            "C",
            "D",
            "M",
        ]

        value = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = []
        sum = 0
        for x in range(len(pattern)):
            total += re.findall(pattern[x], s)
            s = re.split(pattern[x], s)
            s = "".join(s)

        for x in range(len(total)):
            sum += value[total[x]]

        return sum


test = Solution()
a = test.romanToInt("III")
print(a)
