class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        track = []

        for i in range(len(boxes)):
            if boxes[i] == "1":
                track.append(i)

        ans = []
        for i in range(len(boxes)):
            temp = 0
            for num in track:
                temp += abs(num - i)
            ans.append(temp)

        return ans