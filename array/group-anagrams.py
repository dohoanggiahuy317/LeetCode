class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)

        for s in strs:
            track["".join(sorted(list(s)))].append(s)

        return list(track.values())