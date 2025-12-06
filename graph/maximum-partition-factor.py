class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:

        def dist(A, B):
            return abs(A[0] - B[0]) + abs(A[1] - B[1])

        def splitable(m):
            l1, l2 = [], []

            def distribute(i):
                if i >= len(points):
                    if (len(l1) > 0 and len(l2) > 0) and (len(l1) > 1 or len(l2) > 1):
                        return True
                    return False

                this_point = points[i]
                is_l1 = len(l1) == 0 or all(dist(this_point, point1) >= m for point1 in l1)
                is_l2 = len(l2) == 0 or all(dist(this_point, point2) >= m for point2 in l2)

                sub1 = sub2 = False
                if is_l1:
                    l1.append(this_point)
                    sub1 = distribute(i + 1)
                    l1.pop()
                if is_l2:
                    l2.append(this_point)
                    sub2 = distribute(i + 1)
                    l2.pop()

                # print(l1, l2, sub1, sub2)

                return (sub1 or sub2)
            
            return distribute(0)
                
                        
        
        l = 0
        r = 10 ** 9
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if splitable(m):
                # print(ans, m)
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
                
        