class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        best_idx = 0
        best_sum = 0

        for i, row in enumerate(mat):
            row_sum = sum(row)
            if row_sum > best_sum:
                best_sum = row_sum
                best_idx = i

        return [best_idx, best_sum]