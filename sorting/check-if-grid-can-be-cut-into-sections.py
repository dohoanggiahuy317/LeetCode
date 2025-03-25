class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def checkcuts(arr):
            sarr = sorted(arr, key = lambda x: (x[0], -x[1]))
            ans = 0

            curr_start, curr_end = sarr.pop(0)

            while sarr:

                if ans >= 2:
                    return True

                start, end = sarr.pop(0)
                if start >= curr_end:
                    ans += 1
                
                curr_end = max(end, curr_end)

            return True if ans >= 2 else False

        # print(checkcuts(list(map(lambda x: [x[0], x[2]], rectangles ))))
        # print(checkcuts(list(map(lambda x: [x[1], x[3]], rectangles ))))

        return checkcuts(list(map(lambda x: [x[0], x[2]], rectangles ))) or checkcuts(list(map(lambda x: [x[1], x[3]], rectangles )))



                