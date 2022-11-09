import collections

q = collections.deque()

q.append(1)
q.append(2)
q.append(3)

# append at beginning
for _ in range(len(q)-1):
    q.append(q.popleft())

print(q)