class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        for card in sorted(count):
            freq=count[card]
            if freq>0:
                for i in range(card,card+groupSize):
                    if count[i]<freq:
                        return False
                    count[i]-=freq
        return True 


        