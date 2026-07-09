class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for ele in nums:
            map[ele]=map.get(ele,0)+1
        sorted_dic=dict(sorted(map.items(),key=lambda x:x[1],reverse=True))
        return list(sorted_dic.keys())[:k]

        