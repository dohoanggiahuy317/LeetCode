class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l_check = []
        r_check = []

        for i in range(len(target)):
            if target[i] == "L":
                l_check.append(i)
            if target[i] == "R":
                r_check.append(i)
        
        # print(l_check)
        # print(r_check)

        for i in range(len(start)):
            if start[i] == "L":
                if not l_check or i < l_check[0]:
                    return False
                for j in range(l_check[0], i+1):
                    if start[j] == "R":
                        return False
                l_check.pop(0)
            if start[i] == "R":
                if not r_check or i > r_check[0]:
                    return False
                for j in range(i, r_check[0] + 1):
                    if start[j] == "L":
                        return False
                r_check.pop(0)

        return True
                