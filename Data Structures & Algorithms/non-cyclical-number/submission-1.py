class Solution:
    def isHappy(self, n: int) -> bool:
        
        res = n
        visit = set()
        while True:
            nums = [int(ch)*int(ch) for ch in str(res)]
            print(res, nums)
            res = sum(nums)
            if res == 1:
                return True
            if res in visit:
                return False
            visit.add(res)