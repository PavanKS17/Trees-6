# In this approach, we will use a breadth-first search (BFS) to traverse the binary tree level by level.
# We will keep track of the horizontal distance of each node from the root node.
# Nodes that are to the left of the root will have a negative distance, and nodes to the right will have a positive distance.
# TC: O(N) where N is the number of nodes in the tree.
# SC: O(N) for the queue and the map to store the nodes at each horizontal distance.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        dist = deque()
        map = {}
        mini = float('inf')
        maxi = float('-inf')
        q.append(root)
        dist.append(0)
        while q:
            curr = q.popleft()
            curr_dis = dist.popleft()
            mini = min(mini, curr_dis)
            maxi = max(maxi, curr_dis)
            if curr_dis not in map:
                map[curr_dis] = []
            map[curr_dis].append(curr.val)
            if curr.left:
                q.append(curr.left)
                dist.append(curr_dis - 1)
            if curr.right:
                q.append(curr.right)
                dist.append(curr_dis + 1)
        for i in range(mini, maxi + 1):
            res.append(map[i])
        return res