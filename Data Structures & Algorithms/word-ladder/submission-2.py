class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)

        if beginWord == endWord or endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                src = q.popleft()
                if src == endWord:
                    return res
                for i in range(len(src)):
                    pat = src[:i] + "*" + src[i+1:]
                    for word in adj[pat]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
            res+=1

        return 0

                
