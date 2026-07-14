class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoded_string=[]
        # for ele in strs:
        #     encoded_string.append(f"{len(ele)}#{ele}")
        # print(encoded_string)
        # return ''.join(encoded_string)
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

        
