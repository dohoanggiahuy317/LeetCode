class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        m, n = len(img), len(img[0])
        smooth = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                surrounding_sum = img[x][y]
                surrounding_count = 1

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    
                    surrounding_sum += img[nx][ny]
                    surrounding_count += 1
                
                
                smooth[x][y] = surrounding_sum // surrounding_count

        return smooth


