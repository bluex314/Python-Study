# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        # 1 1 1 1 2 2 2 2 3 4  5  6  8   8  9
        # [1, 5, 9]
        # [10, 11, 13]
        # [12, 13, 15)

        def check_less_equal(m) -> int:
            count = 0
            for row in matrix:
                l = 0
                r = len(row)
                while l < r:
                    mid = (r + l) // 2
                    if row[mid] <= m:
                        l = mid + 1
                    else:
                        r = mid
                count += l
            return count

        l = matrix[0][0]
        r = matrix[-1][-1]

        while l < r:
            mid = (r + l)//2
            if check_less_equal(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == '__main__':
    s = Solution()
    m = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(s.kthSmallest(m, k))
