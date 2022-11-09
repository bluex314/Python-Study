# https://leetcode.com/problems/sort-colors/
class Solution:

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]


if __name__=='__main__':
    nums = [1 ,2 ,2 ,2, 0 , 0, 1]
    s = Solution()
    s.sortColors(nums)
    print(nums)
