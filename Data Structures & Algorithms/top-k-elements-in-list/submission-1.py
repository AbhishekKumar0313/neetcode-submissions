class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        map={}
        for ele in nums:
            map[ele]=map.get(ele,0)+1
        bucket=[[] for _ in range(n+1)]
        print(map)
        for key,v in map.items():
            bucket[v].append(key)
        res=[]

        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
            if len(res)==k:
                return res
       


