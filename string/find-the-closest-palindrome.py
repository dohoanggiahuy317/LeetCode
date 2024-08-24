class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)

        if n == "0":
            return "1"
        if l == 1:
            return str(int(n)-1)

        n1 = n[:l//2] + n[:l//2][::-1] if l % 2 == 0 else n[:l//2] + n[l//2] + n[:l//2][::-1]
        n2 = "9" * (l-1)

        if n == n1:

            if n == "11":
                n1 = "22"
            else:
                x = int(n1[l//2])-1
                if n1[l//2] == "0":
                    x = 1
                n1 = n1[:l//2-1] + str(x) * 2 + n1[:l//2-1][::-1] if l % 2 == 0 else n1[:l//2] + str(x) + n1[:l//2][::-1]

        print(n1, n2)

        if abs(int(n1)-int(n)) == abs(int(n2)-int(n)):
            return str(min(int(n1), int(n2)))

        if abs(int(n1)-int(n)) < abs(int(n2)-int(n)):
            return n1
        
        return n2