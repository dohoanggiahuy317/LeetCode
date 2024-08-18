class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        hori, ver = 1, 1
        horizontalCut.sort(reverse = True)
        verticalCut.sort(reverse = True)
        ans = 0

        while horizontalCut and verticalCut:
            # print(horizontalCut, verticalCut)
            if horizontalCut[0] > verticalCut[0]:
                ans += horizontalCut.pop(0) * ver
                hori += 1
            elif horizontalCut[0] < verticalCut[0]:
                ans += verticalCut.pop(0) * hori
                ver += 1
            else:
                if horizontalCut[0] * ver > verticalCut[0] * hori:
                    ans += horizontalCut.pop(0) * ver
                    hori += 1
                else:
                    ans += verticalCut.pop(0) * hori
                    ver += 1


        while horizontalCut:
            ans += horizontalCut.pop(0) * ver
        while verticalCut:
            ans += verticalCut.pop(0) * hori

        return ans 
