class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def f(arr,mid,k):
            cnt = 1
            sums= 0
            for i in range(len(arr)):
                if sums + arr[i] > mid:
                    cnt += 1
                    sums = arr[i]
                else:
                    sums += arr[i]
            return cnt <= k
        low = max(nums)
        high= sum(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if f(nums,mid,k):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
        