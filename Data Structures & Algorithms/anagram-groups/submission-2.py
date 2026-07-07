class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for ele in strs:
            key=tuple(sorted(ele))
            if key not in map:
                map[key]=[ele]
            else:
                map[key].append(ele)
        return list(map.values())

                