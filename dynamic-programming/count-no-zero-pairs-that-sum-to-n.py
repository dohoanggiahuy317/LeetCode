class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        x = len(str(n))
        INT_LIST = [str(i) for i in range(1, 10)]

        def build_num(l):
            nonlocal ans 

            if l > x:
                return

            if numl:
                num = int("".join(numl))
                rem = n - num
                if rem > 0 and "0" not in str(rem):
                    ans += 1

            for i in range(len(INT_LIST)):
                numl.append(INT_LIST[i])
                build_num(l + 1)
                numl.pop()

        numl = []
        ans = 0
        build_num(0)
        

        return ans
