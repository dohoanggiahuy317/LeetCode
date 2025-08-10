

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        START_X, START_Y, INIT_CUT = 0, 0, 0
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        WALL, EMPTY = 0, 1
        m, n = len(forest), len(forest[0])

        tree_list = []
        for i, row in enumerate(forest):
            for j, tree in enumerate(row):
                if tree != WALL and forest[i][j] != EMPTY:
                    tree_list.append(forest[i][j])
        tree_list.sort()
        
        cut_idx = 0
        num_tree = len(tree_list)
        queue = deque([(START_X, START_Y, cut_idx)])
        reachable = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                print(queue)
                c_x, c_y, c_idx = queue.popleft()
                n_idx = c_idx

                if forest[c_x][c_y] == tree_list[c_idx]:
                    n_idx = c_idx + 1

                if n_idx == num_tree:
                    return step

                for i, j in DIRECTIONS:
                    n_x, n_y = c_x + i, c_y + j

                    if not (0 <= n_x < m and 0 <= n_y < n):
                        continue

                    if forest[n_x][n_y] == WALL:
                        continue

                    if (n_x, n_y, n_idx) in reachable:
                        continue

                    queue.append((n_x, n_y, n_idx))
                    reachable.add((n_x, n_y, n_idx))

            step += 1

        return -1