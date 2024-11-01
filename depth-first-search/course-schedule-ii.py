class Node:
    def __init__(self, val):
        self.val = val
        self.parent = []
        self.child = None

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        nodes = {}
        for i in range(numCourses):
            nodes[i] = Node(i)

        for high, pre in prerequisites:
            nodes[pre].parent.append(nodes[high])
            nodes[high].child = nodes[pre]

        sta = []
        visited = [False] * numCourses

        def addSta(curr):
            nonlocal visited

            if visited[curr.val]:
                return
            
            visited[curr.val] = True
            if curr.parent:
                for par in curr.parent:
                    addSta(par)

            sta.append(curr.val)

        ans = []

        for i in range(numCourses):
            if not visited[i] and not nodes[i].child:
                addSta(nodes[i])
                while sta:
                    ans.append(sta.pop(-1))

        return ans


        