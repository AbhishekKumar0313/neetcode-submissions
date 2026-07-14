class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        i=0
        while i<len(s):
            k=i
            while s[k]!='#':
                k+=1
            stringlen=int(s[i:k])
            decoded_string.append(s[k+1:k+1+stringlen])
            i=k+1+stringlen
        return decoded_string

        
