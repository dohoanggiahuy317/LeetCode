class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand or len(hand) % groupSize != 0:
            return False

        hand.sort()

        while len(hand):
            s = hand[0]

            for _ in range(groupSize):
                if s not in hand:
                    return False
                
                hand.remove(s)
                s += 1
        
        return True