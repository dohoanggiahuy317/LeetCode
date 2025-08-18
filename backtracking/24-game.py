class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        def pc(a, b):    
            x = [a + b, a - b, b - a, a * b]
            if a:
                x.append(b/a)
            if b:
                x.append(a/b)
            return x
        
        def check(cards):   
            if len(cards) == 1:
                return abs(cards[0] - 24) <= 0.1
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    newList = [number for k, number in enumerate(cards) if (k != i and k != j)]
                    for x in pc(float(cards[i]), float(cards[j])):
                        newList.append(x)
                        if check(newList):
                            return True
                        newList.pop()
            return False
        return check(cards)