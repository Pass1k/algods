# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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