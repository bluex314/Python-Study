# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (r + l) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    s= Solution()
    print(s.findMin(nums))