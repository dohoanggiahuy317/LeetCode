class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_li = path.split("/")
        ans = []

        for element in path_li:
            if element == "." or element == "":
                continue
            elif element == "..":
                if ans:
                    ans.pop(-1)
            else:
                ans.append(element)

        # print(ans)
        return "/" + "/".join(ans)