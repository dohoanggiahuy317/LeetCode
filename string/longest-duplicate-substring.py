class Solution:
    def longestDupSubstring(self, s: str) -> str:
        seen = {(0, 0)}   
        endings = {(0, 0)}  
        best = (0, 0)        

        for ch in s:
            val = ord(ch) - ord("a")
            new_endings = {(0, 0)} 
            for num, length in endings:
                new_num = num * 26 + val
                new_len = length + 1

                if (new_num, new_len) in seen and new_len > best[1]:
                    best = (new_num, new_len)

                new_endings.add((new_num, new_len))
                seen.add((new_num, new_len))

            endings = new_endings

        def decode(num, length):
            chars = []
            for _ in range(length):
                chars.append(chr(ord("a") + (num % 26)))
                num //= 26
            return "".join(reversed(chars))

        return decode(best[0], best[1])