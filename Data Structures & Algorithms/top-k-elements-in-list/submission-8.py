import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = set()
        hashmap = dict()
        heap = []
        result = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            hashmap[i] += 1
        
        for i, v in hashmap.items():
            heapq.heappush(heap, (-v, i))
        heap = heapq.nsmallest(k, heap)
        
        for i in heap:
            result.append(i[1])
        return result
