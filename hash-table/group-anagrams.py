class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary [key: [str1, str2, ...]] trong d str1, str2, ... la anagram
        anagrams = defaultdict(list)

        # loop qua tung word trong strs
        for word in strs:
            # sort word
            sorted_word = "".join(sorted(list(word)))

            # look up cai sorted word trong dict vaf them vao cai list tuong ung
            anagrams[sorted_word].append(word)


        #return dict.values()
        return list(anagrams.values())
