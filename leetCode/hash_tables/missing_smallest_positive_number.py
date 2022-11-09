# https://leetcode.com/problems/first-missing-positive/

def missing_smallest_positive(nums):
    arr_len = len(nums)
    for i in range(arr_len):
        if nums[i] > arr_len or nums[i] < 1:
            nums[i] = 0
    for i in range(arr_len):
        v = abs(nums[i]) - 1
        if nums[v] > 0:
            nums[v] *= -1
    print(nums)
    for i in range(arr_len):
        if nums[i] >= 0:
            return i + 1
    return arr_len + 1


if __name__ == '__main__':
    nums = [0,1,2]
    ans = missing_smallest_positive(nums)
    print(ans)