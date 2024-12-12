class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        x, y = 0, 0
        
        def check_path(visited, x, y):
            nonlocal grid

            prevx, prevy = -1, -1

            while True:
                # print(x, y, visited) 
                if x == m-1 and y == n-1:
                    break

                if (x, y) in visited:
                    return False

                prevx, prevy = x, y
                visited.add((x, y))

                if grid[x][y] == 1:
                    if (y == 0 and (x, y+1) in visited) or (y == n-1 and (x, y-1) in visited) or ((x, y-1) in visited and (x, y+1) in visited) or (n == 1):
                        return False
                    if (x, y+1) in visited:
                        x, y = x, y-1
                        if grid[x][y] not in {1, 4, 6}:
                            return False
                    if (x, y-1) in visited:
                        x, y = x, y+1
                        if grid[x][y] not in {1, 5, 3}:
                            return False

                elif grid[x][y] == 2:
                    if (x == 0 and (x+1, y) in visited) or (x == m-1 and (x-1, y) in visited) or ((x-1, y) in visited and (x+1, y) in visited) or (m == 1):
                        return False
                    if (x+1, y) in visited:
                        x, y = x-1, y
                        if grid[x][y] not in {2, 3, 4}:
                            return False
                    if (x-1, y) in visited:
                        x, y = x+1, y
                        if grid[x][y] not in {2, 5, 6} :
                            return False

                elif grid[x][y] == 3:
                    if (x == m-1 and (x, y-1) in visited) or (y == 0 and (x+1, y) in visited) or (x == m-1 and y == 0) or ((x+1, y) in visited and (x, y-1) in visited):
                        return False
                    if (x+1, y) in visited:
                        x, y = x, y-1
                        if grid[x][y] not in {1, 4, 6}:
                            return False
                    if (x, y-1) in visited:
                        x, y = x+1, y
                        if grid[x][y] not in {2, 5, 4}:
                            return False

                elif grid[x][y] == 4:
                    if (x == m-1 and (x, y+1) in visited) or (y == n-1 and (x+1, y) in visited) or (x == m-1 and y == n-1) or ((x+1, y) in visited and (x, y+1) in visited):
                        return False
                    if (x+1, y) in visited:
                        x, y = x, y+1
                        if grid[x][y] not in {1, 3, 5}:
                            return False
                    if (x, y+1) in visited:
                        x, y = x+1, y
                        if grid[x][y] not in {2, 5, 6}:
                            return False
        
                elif grid[x][y] == 5:
                    if (x == 0 and (x, y-1) in visited) or (y == 0 and (x-1, y) in visited) or (x == 0 and y == 0) or ((x-1, y) in visited and (x, y-1) in visited):
                        return False
                    if (x-1, y) in visited:
                        x, y = x, y-1
                        if grid[x][y] not in {1, 4, 6}:
                            return False
                    if (x, y-1) in visited:
                        x, y = x-1, y
                        if grid[x][y] not in {2, 3, 4}:
                            return False

                elif grid[x][y] == 6:
                    if (x == 0 and (x, y+1) in visited) or (y == n-1 and (x-1, y) in visited) or (x == 0 and y == n-1) or ((x-1, y) in visited and (x, y+1) in visited):
                        return False
                    if (x-1, y) in visited:
                        x, y = x, y+1
                        if grid[x][y] not in {1, 3, 5}:
                            return False
                    if (x, y+1) in visited:
                        x, y = x-1, y
                        if grid[x][y] not in {2, 3, 4}:
                            return False


            return True


        if grid[x][y] == 1 or grid[x][y] == 3 :
            return check_path({(0, -1)}, 0, 0)
        if grid[x][y] == 2 or grid[x][y] == 6:
            return check_path({(-1, 0)}, 0, 0)
        if grid[x][y] == 5:
            return False
        if grid[x][y] == 4:
            return check_path({(0, 0)}, 1, 0) or check_path({(0, 0)}, 0, 1)
