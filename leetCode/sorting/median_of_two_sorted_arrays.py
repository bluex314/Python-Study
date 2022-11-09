# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        # odd length
        l = r = 0
        m = (len(nums1) + len(nums2))//2 - 1 # from 0 to len to merged arrays
        while True:
            if l+r == m:
                if l < len(nums1):
                    return nums1[l]
                return nums2[r]

            if nums1[l] <= nums2[r]:
                l += 1
            else:
                r += 1


        return m


if __name__ =='__main__':
    nums2 = [1, 2, 5, 7, 9]
    nums1 = [4, 6, 8]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))