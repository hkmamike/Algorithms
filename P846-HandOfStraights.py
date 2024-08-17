class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        groupCnt = len(hand) // groupSize
        groups = []

        hand.sort()
        for i, card in enumerate(hand):
            inserted = False
            for j, group in enumerate(groups):
                if group[-1] + 1 == card:
                    groups[j].append(card)
                    inserted = True
                    if len(groups[j]) == groupSize:
                        groups.pop(j)
                    break
            if not inserted:
                groups.append([card])
                if len(groups) > groupCnt:
                    return False
        return len(groups) == 0