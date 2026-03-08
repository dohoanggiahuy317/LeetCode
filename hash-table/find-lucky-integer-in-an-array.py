class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_counter = Counter(arr)
        ans = -1

        for num, freq in arr_counter.items():
            if num == freq and num > ans:
                ans = num

        return ans
        