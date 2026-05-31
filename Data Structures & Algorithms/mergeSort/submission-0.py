# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:

        i = 0
        j = 0
        result = []

        while i <= len(left)-1 and j <= len(right) -1:
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result



    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs

        # middle
        m = len(pairs)//2

        # divide
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        # merge
        return self.merge(left, right)

