class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)

        if n == "0":
            return "1"
        if l == 1:
            return str(int(n)-1)


        x = int(n[l//2])-1 if l%2==1 else int(n[l//2-1])-1
        if n[l//2] == "0":
            x = 1
        n12 = n[:l//2-1] + str(x) * 2 + n[:l//2-1][::-1] if l % 2 == 0 else n[:l//2] + str(x) + n[:l//2][::-1]

        x = int(n[l//2])+1 if l%2==1 else int(n[l//2-1])+1
        if n[l//2] == "9":
            x = 0
        n11 = n[:l//2-1] + str(x) * 2 + n[:l//2-1][::-1] if l % 2 == 0 else n[:l//2] + str(x) + n[:l//2][::-1]
        n1s = n12 if abs(int(n12) - int(n)) <= abs(int(n) - int(n11)) else n11
        print(n11, n12)

        n1x = n[:l//2] + n[:l//2][::-1] if l % 2 == 0 else n[:l//2] + n[l//2] + n[:l//2][::-1]
        

        n1 = n1s if abs(int(n1s) - int(n)) <= abs(int(n) - int(n1x)) else n1x

        n2 = "9" * (l-1)
        n3 = "1" + "0"* (l-1) + "1"

        if n == n1:
            if n == "11":
                n1 = "22"
            else:
                x = int(n[l//2])-1 if l%2==1 else int(n[l//2-1])-1
                if n[l//2] == "0":
                    x = 1
                n12 = n[:l//2-1] + str(x) * 2 + n[:l//2-1][::-1] if l % 2 == 0 else n[:l//2] + str(x) + n[:l//2][::-1]

                x = int(n[l//2])+1 if l%2==1 else int(n[l//2-1])+1
                if n[l//2] == "9":
                    x = 0
                n11 = n[:l//2-1] + str(x) * 2 + n[:l//2-1][::-1] if l % 2 == 0 else n[:l//2] + str(x) + n[:l//2][::-1]

                n1 = n12 if abs(int(n12) - int(n)) <= abs(int(n) - int(n11)) else n11

        print(n1, n2, n3)

        d1 = abs(int(n1)-int(n))
        d2 = abs(int(n2)-int(n))
        d3 = abs(int(n3)-int(n))

        l = [(d1, n1), (d2, n2), (d3, n3)]

        l.sort(key = lambda x: (int(x[0]), int(x[1])))

        return l[0][1]