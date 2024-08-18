class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        iter = 0
        i = 1
        ans = []
        while iter < len(target) and i < n+1:
            if target[iter] == i:
                ans.append("Push")
                iter += 1
                i += 1
            else:
                i += 1
                ans.append("Push")
                ans.append("Pop")

        return ans