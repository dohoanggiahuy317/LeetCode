from collections import Counter

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        d = defaultdict(lambda: -1)
        d["0000"] = 0
        visited = set(["0000"])
        for x in deadends:
            visited.add(x)
        q = ["0000"]

        def bfs(curr):
            nonlocal d, visited, q

            while len(q) > 0:
                temp = q.pop(0)

                num11 = str( (int(temp[0]) + 1) % 10 ) + temp[1:]
                num12 = str( (int(temp[0]) + 9) % 10 ) + temp[1:]
                num21 = temp[:1] + str( (int(temp[1]) + 1) % 10 ) + temp[2:]
                num22 = temp[:1] + str( (int(temp[1]) + 9) % 10 ) + temp[2:]
                num31 = temp[:2] + str( (int(temp[2]) + 1) % 10 ) + temp[3:]
                num32 = temp[:2] + str( (int(temp[2]) + 9) % 10 ) + temp[3:]
                num41 = temp[:3] + str( (int(temp[3]) + 1) % 10 )
                num42 = temp[:3] + str( (int(temp[3]) + 9) % 10 )

                li = [num11, num12, num21, num22, num31, num32, num41, num42]
                for neigh in li:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
                        d[neigh] = d[temp] + 1

                if temp == target:
                    return


        bfs("0000")
        return d[target]

        

            