class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 1
        
        ans = 0
        i = 0

        while i < len(arr)-1:
            if arr[i] < arr[i + 1]:
                ans += 1
                i += 1
                continue
            
            j = i + 1
            while j < len(arr) and arr[j] < arr[i]:
                j += 1

            ans += 1
            i = j

        # print(i)

        return ans + 1 if i == len(arr) - 1 else ans