START_X, START_Y, INIT_CUT = 0, 0, 0
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        tree_list = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    tree_list.append(forest[i][j])
        tree_list.sort()
        cut_idx = 0

        queue = deque([(START_X, START_Y, cut_idx)])
        reachable = set(queue)
        step = 0


# 4 2 3
# 0 0 1
# 7 6 5
        while queue:
            for _ in range(len(queue)):
                print(queue)
                cx, cy, cut_idx = queue.popleft()

                if forest[cx][cy] == tree_list[cut_idx]:
                    cut_idx += 1

                if cut_idx == len(tree_list):
                    return step

                for i, j in DIRECTIONS:
                    nx, ny = cx + i, cy + j

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if forest[nx][ny] == 0:
                        continue

                    if (nx, ny, cut_idx) in reachable:
                        continue

                    queue.append((nx, ny, cut_idx))
                    reachable.add((nx, ny, cut_idx))

            step += 1

        return -1