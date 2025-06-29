class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        unvowell = defaultdict(str)
        uncasel = defaultdict(str)
        wordset = set()
        for word in wordlist:
            formatword = re.sub(r"[ueoaiUEOAI]", "*", word)
            if formatword.lower() not in unvowell:
                unvowell[formatword.lower()] = word

            if word.lower() not in uncasel:
                uncasel[word.lower()] = word
            
            wordset.add(word)

        ans = []
        for query in queries:
            f = re.sub(r"[ueoaiUEOAI]", "*", query)
            if query in wordset:
                ans.append(query)
            elif query.lower() in uncasel:
                ans.append(uncasel[query.lower()])
            elif f.lower() in unvowell:
                ans.append(unvowell[f.lower()])
            else:
                ans.append("")

        return ans

        