class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key = lambda x: [len(x), x])
        words = sentence.split(" ")

        for i in range(len(words)):
            word = words[i]
            for ori in dictionary:
                if word.startswith(ori):
                    words[i] = ori
                    break
                    
        return " ".join(words)