# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:

    def findKthLargest(self, nums: [int], k: int) -> int:
        k = len(nums) - k

        def quick_sort(l, r):
            pivot = nums[r]
            p = l
            print(nums[p], nums[r])
            for i in range(l,r):
                if nums[i] <= pivot:
                    # this line is so important
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                print(nums)
            nums[p], nums[r] = nums[r], nums[p]
            #print(nums)
            if k < p:
                return quick_sort(l, p-1)
            elif k > p:
                return quick_sort(p+1, r)
            else:
                return nums[p]

        return quick_sort(0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 2, 4]
    print(nums, "\n--------------")
    k = 2
    ans = s.findKthLargest(nums, k)
    print(ans)