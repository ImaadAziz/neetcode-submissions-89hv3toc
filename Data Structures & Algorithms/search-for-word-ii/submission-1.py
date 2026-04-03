class TrieNode():

    def __init__(self):
        self.children = {}
        self.word = ""

    def insert(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word



class Solution:






    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        curr = trie
        res, visit = set(), set()
        def dfs(r, c, curr):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or board[r][c] not in curr.children:
                return
            visit.add((r, c))
            curr = curr.children[board[r][c]]
            if curr.word != "":
                res.add(curr.word)
            dfs(r-1, c, curr)
            dfs(r+1, c, curr)
            dfs(r, c-1, curr)
            dfs(r, c+1, curr)
            visit.remove((r,c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)

        return list(res)
                


                        


    


        
