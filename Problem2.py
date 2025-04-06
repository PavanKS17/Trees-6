# In this approach, we will use level order traversal to serialize and deserialize the binary tree.
# We will use a queue to keep track of the nodes at each level.
# TC: O(n) for both serialize and deserialize
# SC: O(n) for both serialize and deserialize, where n is the number of nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque()
        res = []
        q.append(root)
        while q:
            curr = q.popleft()
            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append('None')
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        strarray = data.split(",")
        if not data:
            return None
        q = deque()
        root = TreeNode(int(strarray[0]))
        q.append(root)
        i = 1
        while q and i < len(strarray):
            curr = q.popleft()
            if strarray[i] != "None":
                curr.left = TreeNode(int(strarray[i]))
                q.append(curr.left)
            i += 1
            if i < len(strarray) and strarray[i] != "None":
                curr.right = TreeNode(int(strarray[i]))
                q.append(curr.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))