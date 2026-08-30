class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content2path = defaultdict(list)

        for path in paths:
            split_by_splash = path.split("/")
            parent_folder_and_files = split_by_splash[-1].split(" ")

            file_dir = "/".join(split_by_splash[:-1] + [parent_folder_and_files[0]])
        
            files = parent_folder_and_files[1:]
            for f in files:
                filename, content = f.split("(")
                content2path[content].append(file_dir + "/" + filename)

        return list(content2path.values())
