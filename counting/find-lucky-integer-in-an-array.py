class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_counter = Counter(arr)
        ans = -1

        for num, freq in arr:
            if num == freq:
                ans = num

        return ans
        