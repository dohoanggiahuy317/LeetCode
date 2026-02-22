class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = []
        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            else:
                last_row = [1]
                for cell1, cell2 in itertools.pairwise(pascal[-1]):
                    last_row.append(cell1 + cell2)
                last_row.append(1)
                pascal.append(last_row)

        return pascal