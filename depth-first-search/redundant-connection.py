class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_li = [False] * (len(edges)+1)
        partition = {}
        track_group = [0] * (len(edges)+1)
        count = 0

        for x in edges:
            # print(track_group)
            # print(partition)
            # print(node_li)
            # print()
            s = x[0]
            e = x[1]

            if track_group[s] == track_group[e] and node_li[s] != False:
                return x

            if node_li[s] == node_li[e] == False:
                count += 1
                partition[count] = [s, e]
                track_group[s] = track_group[e] = count
                node_li[s] = node_li[e] = True
                continue

            max_group = max(track_group[s], track_group[e])
            
            if node_li[s] == node_li[e] == True:
                min_group = min(track_group[s], track_group[e])
                partition[max_group] = partition[max_group] + partition[min_group]

                for node in partition[min_group]:
                    track_group[node] = max_group
                partition[min_group] = []

            partition[max_group].append(s if not node_li[s] else e)
            track_group[s] = track_group[e] = max_group
            node_li[s] = node_li[e] = True
