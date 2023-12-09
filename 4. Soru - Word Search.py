from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word): # Kelimeler Trie'ye eklenir
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True

class WordSearch:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0]) # Tahtadaki konum
        res, visit = set(), set()
        
        def dfs(r, c, node, word): # Depth-First Search
            if (r < 0 or c < 0 or r== ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                
            dfs(r-1, c, node, word) # Yukarı
            dfs(r+1, c, node, word) # Aşağı
            dfs(r, c-1, node, word) # Sola
            dfs(r, c+1, node, word) # Sağa
            
            visit.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

# Örnek
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
words = ["oath","pea","eat","rain"]

solution = WordSearch()
print(solution.findWords(board, words))



































