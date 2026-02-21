class Solution:
    def smallestNumber(self, num: int) -> int:
        res = 0
        if num > 0:
            arr = sorted([int(x) for x in str(num) if x != '0'])
            main_num = arr[0] * (10 ** (len(str(num)) - 1))
            res = main_num + int(''.join(str(x) for x in arr[1:]) if len(arr) > 1 else '0')
               
        elif num < 0:
            num = abs(num)
            arr = sorted([int(x) for x in str(num)])
            arr = arr[::-1]
            res = ''.join(str(x) for x in arr)
            res = int(res) * -1

        return res