class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        cnt = 0
        cnt2 = 0
        people.sort()
        vis = [False]*(r+1)
        while l < r:
            if people[l] + people[r] <= limit:
                cnt += 1
                vis[l] = True
                vis[r] = True
                l+=1
                r-=1
            else:
                r-=1
                cnt2+=1
        
        return cnt+vis.count(False)