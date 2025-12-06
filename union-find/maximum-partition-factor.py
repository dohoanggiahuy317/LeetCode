class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)

        def cal_dist(i, j):
            if i == j:
                return inf

            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        graph = defaultdict()
        for i in range(n):
            for j in range(i + 1, n):
                graph[(i, j)] = cal_dist(i, j)

        group1, group2 = set(), set()
        edges = sorted([(dist, x, y) for (x, y), dist in graph.items()], reverse = True)

        _, a, b = edges.pop()
        group1.add(a)
        group2.add(b)

        while edges:
            _, x, y = edges.pop()
            x_in = (x in group1 or x in group2)
            y_in = (y in group1 or y in group2)

            if x_in and y_in:
                continue

            if x_in:
                if x in group1:
                    group2.add(y)
                else:
                    group1.add(y)
                continue

            if y_in:
                if y in group1:
                    group2.add(x)
                else:
                    group1.add(x)
                continue

            dist_x_1 = min([cal_dist(x, i) for i in group1])
            dist_x_2 = min([cal_dist(x, i) for i in group2])
            dist_y_1 = min([cal_dist(y, i) for i in group1])
            dist_y_2 = min([cal_dist(y, i) for i in group2])

            if min(dist_x_1, dist_y_2) < min(dist_x_2, dist_y_1):
                group1.add(y)
                group2.add(x)
            else:
                group2.add(y)
                group1.add(x)

        dist_group1 = inf
        for i in group1:
            for j in group1:
                dist_group1 = min(dist_group1, cal_dist(i, j))

        dist_group2 = inf
        for i in group2:
            for j in group2:
                dist_group2 = min(dist_group2, cal_dist(i, j))

        return min(dist_group1, dist_group2)



            



