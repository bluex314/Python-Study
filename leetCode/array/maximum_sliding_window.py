import collections


def maxSlidingWindow_kis3(nums):
    l, m, r = 0, 1, 2
    max_sw = []
    num_len = len(nums)-1
    if num_len == 0:
        return [nums[0]]
    elif num_len == 1:
        return [max(nums[0], nums[1])]
    else:
        while (r <= num_len) and (l < m) and (m < r):
            max_sw.append(max(nums[l], nums[m], nums[r]))
            l += 1
            m += 1
            r += 1
    return max_sw

# O(k.(n-k))
def maxSlidingWindow(nums, k):
    kl, kr = 0, k-1
    max_sw = []
    while kr < len(nums):
        max_sw.append(max(nums[kl:kr+1]))
        kl += 1
        kr += 1
    return max_sw

# O(n)
def maxSlidingWindow_optimized(nums, k):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # removing smaller elements
            while q and  nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # removing out of bond values
            if q[0] < l:
                q.popleft()

            # for first k elements
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


if __name__ == '__main__':
    nums = [1, 4, 2, 5,34, 6, 8, 24]
    k = 4
    ans = maxSlidingWindow_optimized(nums, k)
    print(ans)