class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            # num will iterate from the first_num to the (n+1) - (k - len(curr) - 1)
            # since we need space for addtional element after. 
            # So we cannot go up to n
            for num in range(first_num, (n+1) - (k - len(curr) - 1)):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

            return
        
        ans = []
        backtrack([], 1)
        return ans