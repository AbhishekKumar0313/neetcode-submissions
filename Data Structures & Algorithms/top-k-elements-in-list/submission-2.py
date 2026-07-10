class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for ele in nums:
            map[ele]=map.get(ele,0)+1
        heap=[]
        for num in map.keys():
            heapq.heappush(heap,(map[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res