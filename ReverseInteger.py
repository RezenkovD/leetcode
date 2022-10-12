class Solution:
    def reverse(self, x: int) -> int:
        global output_int

        string_x = [str(b) for b in str(x)]

        if len(string_x) == 1:
            if string_x[0] == "0":
                return 0

        if string_x[len(string_x) - 1] == "0":
            string_x.pop(len(string_x) - 1)

        if string_x[0] == "-":
            minus = "-"
            string_x.pop(0)
            output_s = [string_x[x] for x in range(len(string_x) - 1, -1, -1)]
            output_s.insert(0, minus)
            output_int = int("".join(output_s))
        else:
            output_s = [string_x[x] for x in range(len(string_x) - 1, -1, -1)]
            output_int = int("".join(output_s))

        if -(2**31) <= output_int <= (2**31) - 1:
            return output_int
        else:
            return 0


x_ = 1534236469
a = Solution()
print(a.reverse(x=x_))
