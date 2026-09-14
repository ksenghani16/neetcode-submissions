class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=b=c=0
        for triplet in triplets:
            if triplet[0]<=target[0] and triplet[1]<=target[1] and triplet[2]<=target[2]:
                a=max(a,triplet[0])
                b=max(b,triplet[1])
                c=max(c,triplet[2])
        return [a,b,c]==target

        