class Solution:
    def simplifyPath(self, path: str) -> str:
        
        subs = path.split("/")
        subs = list(filter(lambda x: x != "", subs))
        # print(subs)

        ans = []

        for fol in subs:
            if fol == ".":
                continue
            
            elif fol == "..":
                if ans:
                    ans.pop(-1)
            
            else:
                ans.append(fol)

        return '/' + "/".join(ans)

