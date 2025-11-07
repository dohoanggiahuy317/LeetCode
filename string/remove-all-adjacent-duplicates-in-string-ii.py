class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:    
                _, prev = stack[-1]
                stack.append((char, prev + 1))

                if prev + 1 >= k:
                    for _ in range(k):
                        stack.pop()

        return "".join([x[0] for x in stack])