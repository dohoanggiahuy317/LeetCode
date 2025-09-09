class Solution:
    def simplifyPath(self, path: str) -> str:
        
        dir_stack = []

        filenames = [filename for filename in path.split("/") if filename != ""]
        # print(filenames)

        for filename in filenames:
            if filename == ".":
                continue
            if filename == "..":
                if dir_stack:
                    dir_stack.pop()
            else:
                dir_stack.append(filename)

        return "/" + "/".join(dir_stack)
            
