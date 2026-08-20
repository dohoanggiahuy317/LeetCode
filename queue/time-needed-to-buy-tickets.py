class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        total = 0

        for ticket in tickets:
            if ticket < tickets[k]:
                total += ticket
            else:
                total += tickets[k]

        return total