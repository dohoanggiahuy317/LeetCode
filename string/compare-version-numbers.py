class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = list(map(int, version1.split(".")))
        li2 = list(map(int, version2.split(".")))

        for x in range(max( 0, len(li2) - len(li1) )):
            li1.append(0)
        for x in range(max( 0, len(li1) - len(li2) )):
            li2.append(0)

        for i in range(len(li1)):
            if li1[i] > li2[i]:
                return 1
            if li1[i] < li2[i]:
                return -1

        return 0