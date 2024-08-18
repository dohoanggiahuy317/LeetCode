class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        smaller = arr[0] < arr[1]
        ans = 0
        curr = 0

        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if smaller == True:
                    curr = 1
                else:
                    curr += 1
                    smaller = True
                ans = max(ans, curr)

            elif arr[i] > arr[i+1]:
                if smaller == False:
                    curr = 1
                else:
                    curr += 1
                    smaller = False
                ans = max(ans, curr)

            else:
                if arr[i] == arr[i+1]:
                    curr = 0
                    ans = max(ans, curr)
                smaller = arr[i] < arr[i+1]  

        return ans + 1