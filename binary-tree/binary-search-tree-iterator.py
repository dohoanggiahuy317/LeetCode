# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def transversal(self, node):
        if not node:
            return
        
        self.transversal(node.left)
        self.l.append(node.val)
        self.transversal(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.transversal(root)
        self.i = -1

    def next(self) -> int:
        self.i += 1
        return self.l[self.i]

    def hasNext(self) -> bool:
        return self.i != len(self.l) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()