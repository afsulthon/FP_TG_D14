"""
Author: Kelompok 14
- Akmal Sulthon Fathulloh (5025211047)
- Syomeron Ansell Widjaya (5025211250)
- Ilham Insan Wafi (5025211255)
Date: 2023-12-22
Description: Largest Monotonically Increasing Subsequence (LIS) problem.
"""


def lis(nums):
    n = len(nums)
    lis_len = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis_len[i] = max(lis_len[i], lis_len[j] + 1)

    max_len = max(lis_len)
    last_index = lis_len.index(max_len)

    lis = [nums[last_index]]
    cur_len = max_len - 1
    for i in range(last_index - 1, -1, -1):
        if nums[i] < nums[last_index] and lis_len[i] == cur_len:
            lis.insert(0, nums[i])
            cur_len -= 1

    return lis, max_len


nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
lis, lis_len = lis(nums)
print("Sequence:", nums)
print("LIS:", lis)
print("Length of LIS:", lis_len)
