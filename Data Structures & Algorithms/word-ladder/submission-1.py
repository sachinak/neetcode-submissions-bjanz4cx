class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        adj = defaultdict(list)

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
                    pattern = src[:i] + "*" + src[i+1:]
                    for word in adj[pattern]:
                        if word not in visited:
                            q.append(word)
                            visited.add(word)
            res +=1
        return 0

                
