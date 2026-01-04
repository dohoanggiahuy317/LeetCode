class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        di = {i:chr(ord("A")+i) for i in range(26)}

        i=0
        while True:
            if columnNumber-26**i<0:
                i-=1
                break
            columnNumber-=26**i
            i+=1
        
        res=""

        print(columnNumber, i)
        for j in range(i,-1,-1):
            res = res + di[columnNumber//(26**j)]
            columnNumber -= 26**j * (columnNumber//(26**j))
        return res


        
