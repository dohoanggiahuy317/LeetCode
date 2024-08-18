class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = [1]
        s1, s2, s3 = 0, 0, 0

        while len(num) < n:
            # print(num)
            n1 = num[s1] * 2
            n2 = num[s2] * 3
            n3 = num[s3] * 5
            
            num.append(min([n1, n2, n3]))

            if num[-1] == n1:
                s1 += 1
            if num[-1] == n2:
                s2 += 1
            if num[-1] == n3:
                s3 += 1
            
        return num[-1]