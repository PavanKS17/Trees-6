# In this approach , we use an iterative depth-first search (DFS) to traverse the binary search tree (BST).
# TC: O(N) where N is the number of nodes in the tree.
# SC: O(H) where H is the height of the tree, due to the stack space used by the recursion or the stack for iterative DFS.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        s = []
        while root or s:
            while root:
                s.append(root)
                if root.val > low:
                    root = root.left
                else:
                    break
            root = s.pop()
            if root.val >= low and root.val <= high:
                sum = sum + root.val
            root = root.right
        return sum







        # self.total = 0

        # def helper(node):
        #     if not node:
        #         return
        #     if low <= node.val <= high:
        #         self.total += node.val
        #     if node.val < high:
        #         helper(node.right)
        #     if node.val > low:
        #         helper(node.left)

        # helper(root)
        # return self.total
