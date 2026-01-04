from collections import defaultdict
import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        graph = defaultdict(list)
        l = [beginWord] + list(set(wordList))
        for word in l:
            for i in range(n):
                temp = word[:i] + " " + word[i+1:]
                graph[temp].append(word)

        q = []
        heapq.heappush(q, (1, beginWord))
        visited = {beginWord}

        while q:
            val, word = heapq.heappop(q)
            if word == endWord:
                return val
            visited.add(word)

            for i in range(n):
                temp = word[:i] + " " + word[i+1:]

                for neigh in graph[temp]:
                    if neigh not in visited:
                        heapq.heappush(q, (val + 1, neigh))

        return 0

        