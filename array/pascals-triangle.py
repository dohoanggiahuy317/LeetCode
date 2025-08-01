class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        ans = self.generate(numRows - 1)
        new_row = [1] + [ans[-1][i] + ans[-1][i + 1] for i in range(len(ans[-1]) - 1)] + [1]

        return ans + [new_row]