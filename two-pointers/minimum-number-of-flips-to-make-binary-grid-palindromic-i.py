from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        def count_flips_to_palindrome(arr):
            flips = 0
            n = len(arr)
            for i in range(n // 2):
                if arr[i] != arr[n - 1 - i]:
                    flips += 1
            return flips

        def total_flips_to_palindromic_rows(grid):
            return sum(count_flips_to_palindrome(row) for row in grid)

        def total_flips_to_palindromic_columns(grid):
            m, n = len(grid), len(grid[0])
            flips = 0
            for i in range(n):
                column = [grid[j][i] for j in range(m)]
                flips += count_flips_to_palindrome(column)
            return flips

        return min(total_flips_to_palindromic_rows(grid), total_flips_to_palindromic_columns(grid))