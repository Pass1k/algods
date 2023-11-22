import deque

class Solution(object):
    def countNodes(self, root):
        q = deque([root])
        count = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    count += 1
                    q += [node.left]
                    q += [node.right]
        return count