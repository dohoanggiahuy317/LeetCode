START_X, START_Y, INIT_CUT = 0, 0, 0
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        largest_tree = 0
        rem_tree = 0
        for i in range(m):
            for j in range(n):
                largest_tree = max(largest_tree, forest[i][j])
                rem_tree += 1 if forest[i][j] != 0 else 0

        queue = deque([(START_X, START_Y, INIT_CUT, rem_tree)])
        reachable = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                cx, cy, c_largest, c_tree = queue.popleft()

                if c_largest == largest_tree and c_tree == 1:
                    return step

                for i, j in DIRECTIONS:
                    nx, ny = cx + i, cy + j

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if forest[nx][ny] == 0:
                        continue

                    if (nx, ny, c_largest, c_tree) in reachable:
                        continue

                    if forest[nx][ny] < c_largest:
                        continue

                    if forest[nx][ny] > c_largest:
                        queue.append((nx, ny, c_largest, c_tree))
                        reachable.add((nx, ny, c_largest, c_tree))

                        n_largest = forest[nx][ny]
                        n_tree = c_tree - 1

                        queue.append((nx, ny, n_largest, n_tree))
                        reachable.add((nx, ny, n_largest, n_tree))

            step += 1

        return -1