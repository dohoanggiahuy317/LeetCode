class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)

        if l == 1:
            return n

        n1 = n[:l//2] + n[:l//2][::-1] if l % 2 == 0 else n[:l//2] + n[l//2] + n[:l//2][::-1]
        n2 = "9" * (l-1)

        print(n1, n2)

        if abs(int(n1)-int(n)) == abs(int(n2)-int(n)):
            return str(min(int(n1), int(n2)))

        if abs(int(n1)-int(n)) < abs(int(n2)-int(n)):
            return n1
        
        return n2