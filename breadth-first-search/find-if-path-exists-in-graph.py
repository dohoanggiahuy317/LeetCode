class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if len(edges) == 0:
            return True

        par = {}
        groups = {}

        for edge in edges:
            # print(par)
            # print(groups)
            # print()
            x1, x2 = edge

            if x1 not in par and x2 not in par:
                par[x1] = par[x2] = min(x1, x2)
                groups[min(x1, x2)] = set([x1, x2])
            elif x1 in par and x2 in par:
                if par[x1] != par[x2]:
                    new_par = min(par[x1], par[x2])

                    temp = set()
                    for x in groups[par[x1]]:
                        temp.add(x)
                    for x in groups[par[x2]]:
                        temp.add(x)    
                    groups[new_par] = temp

                    for x in groups[par[x1]]:
                        par[x] = new_par
                    for x in groups[par[x2]]:
                        par[x] = new_par  
            else:
                if x1 in par:
                    new_par = min(x2, par[x1])   
                
                    temp = set()
                    for x in groups[par[x1]]:
                        temp.add(x)
                    temp.add(x2)
                    groups[new_par] = temp

                    par[x2] = new_par
                    for x in groups[par[x1]]:
                        par[x] = new_par

                elif x2 in par:
                    new_par = min(x1, par[x2])   
                
                    temp = set()
                    for x in groups[par[x2]]:
                        temp.add(x)
                    temp.add(x1)
                    groups[new_par] = temp

                    par[x1] = new_par
                    for x in groups[par[x2]]:
                        par[x] = new_par

        if source not in par or destination not in par:
            return False

        return par[source] == par[destination]