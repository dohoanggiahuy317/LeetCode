class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        for i in range(len(stickers)):
            newSticker = ""
            for char in stickers[i]:
                if char in target:
                    newSticker += char

            stickers[i] = newSticker

        A = []
        stickers.sort(key = len, reverse = True)
        nStickers = []

        for sticker in stickers:
            stickerCount = Counter(sticker)
            ad = True
            for otherCount in A:
                if otherCount > stickerCount:
                    ad = False
                    break

            if ad:
                A.append(stickerCount)
                nStickers.append("".join(sorted(list(sticker))))

        t_count = collections.Counter(target)


        ans = len(target) + 1

        def search(localAns):
            nonlocal ans, t_count, A
            if localAns >= ans:
                return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    ans = localAns
                return

            currSticker = A.pop()
            used = max((t_count[letter] - 1)//currSticker[letter] + 1 for letter in currSticker)
            used = max(0, used)
            for c in currSticker:
                t_count[c] -= used * currSticker[c]

            search(localAns + used)

            for i in range(used-1, -1, -1):
                for letter in currSticker:
                    t_count[letter] += currSticker[letter] 
                search(localAns + i)

            A.append(currSticker)

        search(0)
        return ans if ans <= len(target) else -1
