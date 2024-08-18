class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []

        ans.append(pref[0])
        curr = ans[0]

        for i in range(1, len(pref)):
            ans.append(curr ^ pref[i])
            curr = curr ^ ans[-1]

        return ans