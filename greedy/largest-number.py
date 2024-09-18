class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def permute(arr, l, r):
            nonlocal ans
            if l >= r:
                print(arr)
                ans = max(ans, "".join(arr))
                return 


            for i in range(l, r):
                arr[i], arr[l] = arr[l], arr[i]
                permute(arr, l+1, r)
                arr[i], arr[l] = arr[l], arr[i]

        ans = "0"
        permute(list(map(str, nums)), 0, len(nums))    

        return ans