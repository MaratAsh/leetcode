from queue import Queue
from typing import Optional


inf = float('inf')

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMonotonicInc(self, less, val, more):
        return less < val < more

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = Queue()
        q.put((-inf, inf, root))

        while not q.empty():
            less, more, node = q.get()
            if not self.isMonotonicInc(less, node.val, more):
                return False
            if node.left:
                if node.left.val >= node.val:
                    return False
                q.put((
                    min(less, node.val),
                    node.val,
                    node.left
                ))
            if node.right:
                if node.right.val <= node.val:
                    return False
                q.put((
                    max(less, node.val),
                    more,
                    node.right
                ))

        return True
