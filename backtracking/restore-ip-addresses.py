class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(k, l):
            if k == 4:
                if l < 4 and l > 0:
                    num1 = s[:subset[0]]
                    num2 = s[subset[0]:subset[0] + subset[1]]
                    num3 = s[subset[0] + subset[1]:subset[0] + subset[1] + subset[2]]
                    num4 = s[subset[0] + subset[1] + subset[2]:]

                    print(num1, num2, num3, num4)
                    
                    if num1.startswith("0") and len(num1) != 1:
                        return
                    if num2.startswith("0") and len(num2) != 1:
                        return
                    if num3.startswith("0") and len(num3) != 1:
                        return
                    if num4.startswith("0") and len(num4) != 1:
                        return

                    if int(num1) > 255 or int(num2) > 255 or int(num3) > 255 or int(num4) > 255:
                        return

                    ans.append(".".join([num1, num2, num3, num4]))
                return

            subset.append(1)
            backtrack(k+1, l-1)
            subset.pop()

            subset.append(2)
            backtrack(k+1, l-2)
            subset.pop()

            subset.append(3)
            backtrack(k+1, l-3)
            subset.pop()

        ans = []
        subset = []
        backtrack(1, len(s))

        return ans