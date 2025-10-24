class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        def dfs(i, g):
            nonlocal holder, ans
            # print(s_li, holder, g)

            if ans != "": # terminate if answer is determined
                return

            if i == len(s):
                if g:
                    ans = "".join(holder)
                return

            if g:
                holder.extend(s_li)
                ans = "".join(holder)
                return
            
            t_char = target[i]

            # Get the equal value if possible
            idx = bisect.bisect_left(s_li, t_char)
            if idx == len(s_li):
                return
            
            s_char = s_li.pop(idx)
            holder.append(s_char)
            dfs(i + 1, s_char > t_char)

            # if not possible then we have to take strictly larget
            s_li.insert(idx, s_char)
            holder.pop()

            idx = bisect.bisect_right(s_li, t_char)
            if idx == len(s_li):
                return
            s_char = s_li.pop(idx)
            holder.append(s_char)
            dfs(i + 1, True)

        s_li = sorted(s)
        holder = []
        ans = ""
        dfs(0, False)

        return ans

