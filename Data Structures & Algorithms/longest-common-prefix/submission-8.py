class TrieNode:
    def __init__(self):
        self.children={}
        self.isend=False
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isend=True
    
    def lcp(self,node,res):
        if node.isend==True or len(node.children)>1:
            return res
        res.append(list(node.children.keys())[0])
        self.lcp(node.children[list(node.children.keys())[0]],res)
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()
        for string in strs:
            trie.insert(string)
        res=trie.lcp(trie.root,[])
        return ''.join(res)