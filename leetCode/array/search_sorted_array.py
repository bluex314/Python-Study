# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):

    while True:
        nlen = len(nums)
        pivot = nlen // 2

        if target == nums[pivot]:
            return nums[pivot]
        elif nums[0] <= nums[pivot] and nums[0] <= target:
            nums = nums[:pivot]
        else:
            nums = nums[pivot:]


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5]
    target = 4
    ans = search(nums, target)
    print(ans)