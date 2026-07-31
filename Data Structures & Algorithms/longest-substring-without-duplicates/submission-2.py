class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        length=0
        seen=set()
        for i in range(len(s)):
            if s[i] not in seen: 
                seen.add(s[i])
            else:
                length=max(length,len(seen))
                while s[left]!=s[i]:
                    seen.remove(s[left])
                    left+=1
                seen.remove(s[left])
                left=i if not seen else  left+1
                seen.add(s[i])
        return max(length,len(seen))


        