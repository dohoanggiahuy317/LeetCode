class Solution:
    def numberOfWays(self, corridor: str) -> int:

        seat, tree = 0, 0
        ans = 1
        valid = False

        for item in corridor:
            if seat == 2:
                valid = True
                if item == "P":
                    tree += 1
                else:
                    ans = ( ans * (tree + 1) ) % (10 ** 9 + 7)
                    tree = 0
                    seat = 1
            else:
                if item == "S":
                    seat += 1
        if seat == 2:
            valid = True
        if seat == 1:
            valid = False
                

        return ans if valid else 0