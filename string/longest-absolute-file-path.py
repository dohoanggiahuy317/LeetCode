class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inp_li = input.split("\n")
        depth = [0] * len(inp_li)

        def count_depth(s):
            count = 0
            for i in range(len(s)):
                if s[i:].startswith("\t"):
                    count += 1
                else:
                    break

            return count

        for i in range(len(depth)):
            depth[i] = count_depth(inp_li[i])

        temp = []
        curr = []
        ans = 0
        for i in range(len(depth)):
            while curr and curr[-1] >= depth[i]:
                curr.pop()
                temp.pop()


            temp.append(inp_li[i][depth[i]:])
            curr.append(depth[i])
            if "." in temp[-1]:
                ans = max(ans, len("/".join(temp)))

        return ans