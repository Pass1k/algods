from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.appendleft(0)    
dq.append(6)
print(dq)

dq.pop()
dq.popleft()

print(dq)