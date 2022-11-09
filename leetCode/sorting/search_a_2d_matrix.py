# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def kthSmallest(self, matrix, target: int) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        # 1 1 1 1 2 2 2 2 3 4  5  6  8   8  9
        # [1, 5, 9]
        # [10, 11, 13]
        # [12, 13, 15)

        for row in matrix:
            l = 0
            r = len(row)-1
            while l <= r:
                mid = (r + l) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    l = mid + 1
                else:
                    r = mid-1
        return False


if __name__ == '__main__':
    s = Solution()
    m = [[1]]
    k = 1
    print(s.kthSmallest(m, k))
