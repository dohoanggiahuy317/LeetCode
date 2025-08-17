class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr

        target = -1
        j = -1
        for t in range(i + 1, n):
            if arr[t] < arr[i] and arr[t] > target:
                target = arr[t]
                j = t

        arr[i], arr[j] = arr[j], arr[i]
        return arr