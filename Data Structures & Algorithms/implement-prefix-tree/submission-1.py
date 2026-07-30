class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                temp = PrefixTree()
                node.children[ch] = temp
            
            node = node.children[ch]
            
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True if node.isEnd else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True 
        
        