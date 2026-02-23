class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip = []
        for row in image:
            flip.append(row[::-1])

        invert = []
        for row in flip:
            invert_row = []

            for cell in row:
                invert_row.append(1 if cell == 0 else 0)
            
            invert.append(invert_row)

        return invert