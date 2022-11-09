# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        nl = [i for i in range(1, n+1)]
        a = []
        def b(nl, k, i):
            l = [nl[0]]
            if i == len(nl):
                a.append(l.copy())
                return
            while len(l) <= k:
                l.append(nl[i+1])
                return
        b(nl, k, 0)
        return a

if __name__ == '__main__':
    print(Solution().combine(4, 2))