class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]

        node = root
        while node.left:
            node = node.left
            self.stack.append(node)
            

    def next(self) -> int:
        smallest_node = self.stack.pop()

        if smallest_node.right:
            next_node = smallest_node.right
            self.stack.append(next_node)

            while next_node.left:
                next_node = next_node.left
                self.stack.append(next_node)

        return smallest_node.val

    def hasNext(self) -> bool:
        if not self.stack:
            return False
        return True