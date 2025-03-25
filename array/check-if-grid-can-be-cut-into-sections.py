class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def checkcuts(arr):
            sarr = sorted(arr, key = lambda x: (x[0], x[1]))
            ans = 0

            curr_end = sarr.pop(0)[1]
            last_start = sarr.pop(-1)[0]

            while arr:
                if ans >= 2:
                    return True

                start, end = arr.pop(0)
                if start >= curr_end:
                    ans += 1
                
                curr_end = max(end, curr_end)

                if not arr and end <= last_start:
                    ans += 1

            return True if ans >= 2 else False

        # print(checkcuts(list(map(lambda x: [x[0], x[2]], rectangles ))))
        # print(checkcuts(list(map(lambda x: [x[1], x[3]], rectangles ))))

        return checkcuts(list(map(lambda x: [x[0], x[2]], rectangles ))) or checkcuts(list(map(lambda x: [x[1], x[3]], rectangles )))



                