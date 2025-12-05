class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def backtrack():
            nonlocal found
            print(cards)

            if found:
                return
            
            if len(cards) == 1:
                if abs(cards[0] - 24) <= 0.1:
                    found = True
                return 

            for i in range(len(cards)):
                num1 = cards[i]
                for j in range(i + 1, len(cards)):
                    if i == j:
                        continue

                    num2 = cards[j]
                    cards.pop(j)

                    cards[i] = num1 + num2
                    backtrack()

                    cards[i] = num1 - num2
                    backtrack()

                    cards[i] = num2 - num1
                    backtrack()

                    cards[i] = num1 * num2
                    backtrack()

                    if num2 != 0:
                        cards[i] = num1 / num2
                        backtrack()
                    
                    if num1 != 0:
                        cards[i] = num2 / num1
                        backtrack()
                    
                    cards.insert(j, num2)
                    cards[i] = num1
                    
                    


        found = False
        backtrack()
        return found