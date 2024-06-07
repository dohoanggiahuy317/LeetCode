class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = ""
        num = "0" * (4 - len(str(num))) + str(num)
        ind = 0

        while int(num) > 0:
            # print(num, int(num), ans)
            if num[ind] == "0":
                ind += 1
                continue
            elif num[ind] == "4":
                if ind == 1:
                    ans += "CD"
                elif ind == 2:
                    ans += "XL"
                elif ind == 3:
                    ans += "IV"
                num = num[:ind] + "0" + num[ind+1:]

            elif num[ind] == "9":
                if ind == 1:
                    ans += "CM"
                elif ind == 2:
                    ans += "XC"
                elif ind == 3:
                    ans += "IX"
                
                num = num[:ind] + "0" + num[ind+1:]
            else:
                if int(num) >= 1000:
                    while int(num) >= 1000:
                        num = int(num) - 1000
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "M"
                elif int(num) >= 500:
                    while int(num) >= 500:
                        num = int(num) - 500
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "D"              
                elif int(num) >= 100:
                    while int(num) >= 100:
                        num = int(num) - 100
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "C" 
                elif int(num) >= 50:
                    while int(num) >= 50:
                        num = int(num) - 50
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "L" 
                elif int(num) >= 10:
                    while int(num) >= 10:
                        num = int(num) - 10
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "X" 
                elif int(num) >= 5:
                    while int(num) >= 5:
                        num = int(num) - 5
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "V" 
                elif int(num) >= 1:
                    while int(num) >= 1:
                        num = int(num) - 1
                        num = "0" * (4 - len(str(num))) + str(num)
                        ans += "I"

            if num[ind] == "0":
                ind += 1

        return ans

        