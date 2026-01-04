class Solution:
    def recoverFromPreorder(self, traversal):
        stack = []
        index = 0
        root = None

        while index < len(traversal):
            # Count the number of dashes
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract the node value
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the current node
            node = TreeNode(value)

            # If depth is 0, it's the root
            if depth == 0:
                root = node
            else:
                # Pop nodes from the stack until we find the parent
                while len(stack) > depth:
                    stack.pop()

                # Attach the node to the parent
                if stack[-1][0].left == None:
                    stack[-1][0].left = node
                else:
                    stack[-1][0].right = node

            # Push the current node and its depth onto the stack
            stack.append((node, depth))

        return root