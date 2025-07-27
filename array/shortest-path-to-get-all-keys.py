from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
KEY_DICT = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
}

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # find k


        # queue = (x, y, key_state, step)


        # while
        #     step += 1
        #     for
        # if find all key


        m, n = len(grid), len(grid[0])
        k = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                if grid[i][j].islower():
                    k += 1

        queue = deque()
        init_state = (start[0], start[1], 0)
        queue.append(init_state)
        visited = set()
        step = 0


        while queue:
            for _ in range(len(queue)):
                x, y, key = queue.popleft()
                visited.add((x, y, key))
                # print(x, y, bin(key))

                # check co full key
                if key == (1 << k) - 1:
                    # print(k)
                    # print(bin(key), bin((1 << k) - 1))
                    # print("FULL")
                    return step
                
                # di den cac avalabile oo ben canh voi key state moi
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if grid[nx][ny] == "#":
                        continue
                    if (nx, ny, key) in visited:
                        continue
                    if grid[nx][ny].isupper():
                        if not key >> KEY_DICT[grid[nx][ny].lower()] & 1:
                            continue
                    
                    new_key = key
                    if grid[nx][ny].islower():
                        new_key = key | (1 << KEY_DICT[grid[nx][ny]])
                    queue.append( (nx, ny, new_key) )

            step += 1

        return -1
# @...a
# .###A
# b.BCc
