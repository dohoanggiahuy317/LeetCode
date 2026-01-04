class Solution:
    def countBits(self, n: int) -> List[int]:
        li = [i for i in range(n+1)]
        
        for idx in range(n+1):
            bin_ele = bin(li[idx])[2:]
            
            counter = 0
            
            for num in bin_ele:
                if num == "1":
                    counter += 1
            
            li[idx] = counter
            
        return li