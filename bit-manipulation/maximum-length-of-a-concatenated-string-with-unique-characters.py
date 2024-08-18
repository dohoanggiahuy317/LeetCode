class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        ans = 0

        def backtrack(s, i):
            nonlocal ans
            if i >= len(arr):
                return
            # print(s)
            
            b = True
            temp = set(list(s))
            for char in list(arr[i]):
                if char in temp:
                    b = False
                else:
                    temp.add(char)

            if b:
                ans = max(len(s + arr[i]), ans)
                backtrack(s+arr[i], i + 1)
            
            backtrack(s, i+1)

        backtrack("", 0)

        return ans