# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def dfs(root, res, tmp=""):
            tmp += "{} ".format(str(root.val))
            if not (root.left or root.right):
                res.append("->".join(tmp.split(" "))[:-2])
                tmp = ""
                return 
            if root.left:
                dfs(root.left, res, tmp)    
            if root.right:
                dfs(root.right, res, tmp)
        dfs(root, result)
        return result    