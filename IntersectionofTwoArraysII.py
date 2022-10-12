from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list(set(nums1) & set(nums2))
        print(intersection)
        count_dict_1 = {}
        count_dict_2 = {}

        for x in range(len(intersection)):
            count_dict_1[intersection[x]] = 0
            for y in range(len(nums1)):
                if intersection[x] == nums1[y]:
                    count_dict_1[intersection[x]] += 1

        for x in range(len(intersection)):
            count_dict_2[intersection[x]] = 0
            for y in range(len(nums2)):
                if intersection[x] == nums2[y]:
                    count_dict_2[intersection[x]] += 1

        output_list = []

        for x in range(len(intersection)):

            if count_dict_1[intersection[x]] > count_dict_2[intersection[x]]:
                for y in range(count_dict_2[intersection[x]]):
                    output_list.append(intersection[x])
            elif count_dict_1[intersection[x]] == count_dict_2[intersection[x]]:
                for y in range(count_dict_1[intersection[x]]):
                    output_list.append(intersection[x])
            else:
                for y in range(count_dict_1[intersection[x]]):
                    output_list.append(intersection[x])

        return output_list


a = Solution()
a.intersect([1, 2, 2, 2, 1, 1, 12, 122, 12], [2, 2, 1, 1, 12, 12])
