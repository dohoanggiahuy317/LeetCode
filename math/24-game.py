class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def backtrack():
            nonlocal found
            print(cards)

            if found:
                return
            
            if len(cards) == 1:
                if cards[0] == 24:
                    found = True
                return 

            for i1 in range(len(cards)):
                num1 = cards[i1]
                for j in range(len(cards)):
                    i = i1
                    if i1 == j:
                        continue

                    if i1 > j:
                        i -= 1

                    num2 = cards[j]

                    cards.pop(j)

                    cards[i] = num1 - num2
                    backtrack()

                    cards[i] = num1 * num2
                    backtrack()

                    cards[i] = num1 + num2
                    backtrack()

                    if num2 != 0:
                        cards[i] = num1 / num2
                        backtrack()

                    cards[i] = num1
                    cards.insert(j, num2)


        found = False
        backtrack()
        return found