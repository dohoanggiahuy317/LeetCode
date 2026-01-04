class Solution:
    def reverseBits(self, n: int) -> int:
        
        #convert to binary and add "0" to make 32 bits
        deci_non32 = bin(n)[2:]
        deci_32 = "0"*(32-len(deci_non32)) + deci_non32
        
        #reverse the string and convert to int
        rev_res = deci_32[::-1]
        res = int(rev_res, 2)
        
        return res