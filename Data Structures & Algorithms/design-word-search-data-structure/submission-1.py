class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.word


        return dfs(0, node)

           

