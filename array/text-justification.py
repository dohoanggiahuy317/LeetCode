class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def line_handle(arr):
            nonlocal maxWidth
            if len(arr) == 1:
                return arr[0] + " " * (maxWidth - len(arr[0]))
            
            cur_len = sum(list(map(len, arr)))
            av = (maxWidth - cur_len) // (len(arr) - 1)
            lf = (maxWidth - cur_len) % (len(arr) - 1)

            ans = ""
            for i in range(len(arr) - 1):
                ans += arr[i]
                ans += " " * av
                if lf > 0:
                    ans = ans + " "
                    lf -= 1
            ans += arr[-1]
            return ans
 
        def last_line(arr):
            nonlocal maxWidth
            curr = " ".join(arr)
            return curr + " " * (maxWidth - len(curr))


        i = -1
        ans = []
        while i < len(words):
            curr = []
            scurr = 0
            while scurr < maxWidth and i < len(words):
                if i < len(words) - 1 and scurr + len(words[i + 1]) <= maxWidth:
                    scurr += len(words[i+1])
                    curr.append(words[i+1])
                    i += 1
                    scurr += 1
                else:
                    break
            # print(curr, i)
            if i >= len(words)-1:
                ans.append(last_line(curr))
                return ans
            else:
                ans.append(line_handle(curr))

        return ans
