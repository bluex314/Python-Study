# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> []:
        res = []

        def backtrack(openN, closeN, stack):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                backtrack(openN+1, closeN, stack + ["("])
            if closeN < openN:
                backtrack(openN, closeN+1, stack + [")"])
        backtrack(0, 0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    n = 3
    o = s.generateParenthesis(n)
    print(o)