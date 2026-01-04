class Solution:
    def largestInteger(self, num: int) -> int:
        oddEven = ""
        listNum = list(str(num))
        even = []
        odd = []
        res = ""
        
        for i in listNum:
            if int(i) % 2 == 0:
                oddEven += "0"
                even.append(i)
            else:
                oddEven += "1"
                odd.append(i)
                
        even.sort(reverse = True)
        odd.sort(reverse = True)
        for i in oddEven:
            if i == "0":
                res += even[0]
                even.pop(0)
            else:
                res += odd[0]
                odd.pop(0)
                
        return int(res)
        
        