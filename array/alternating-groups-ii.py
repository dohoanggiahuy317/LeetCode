class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        temp = colors + colors[0:k-1]
        # print(temp)
        odd = temp[0::2]
        even = temp[1::2]
        ans = 0
        i = k//2

        
        if k % 2 == 1:
            while i < len(temp) - k//2:
                # print(temp[i-k//2: i+k//2+1], temp[i-k//2: i+k//2+1:2], temp[i-k//2 + 1: i+k//2+1: 2])
                if  len(set(temp[i-k//2 : i+k//2+1 : 2])) == 1 and len(set(temp[i-k//2 + 1 : i+k//2+1 : 2])) == 1 and temp[i-k//2] != temp[i-k//2+1]:
                    ans += 1
                    while i+k//2+1 < len(temp) and temp[i+k//2+1] == temp[i+k//2-1]:
                        # print("haha", temp[i-k//2: i+k//2+1], temp[i-k//2: i+k//2+1:2], temp[i-k//2 + 1: i+k//2+1: 2])
                        i += 1
                        ans += 1
                i += 1
        else:
            while i < len(temp) - k//2 + 1:
                # print(temp[i-k//2: i+k//2], temp[i-k//2: i+k//2:2], temp[i-k//2 + 1: i+k//2: 2])
                if  len(set(temp[i-k//2 : i+k//2 : 2])) == 1 and len(set(temp[i-k//2 + 1 : i+k//2 : 2])) == 1 and temp[i-k//2] != temp[i-k//2+1]:
                    ans += 1
                    while i+k//2 < len(temp) and temp[i+k//2] == temp[i+k//2-2]:
                        i += 1
                        ans += 1
                i += 1

        return ans