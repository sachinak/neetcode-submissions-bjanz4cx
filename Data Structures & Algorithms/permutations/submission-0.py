class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res=[]
        pick = [False]*len(nums)
        subsets = []

        def rec():
            for i in range(len(nums)):
                if len(subsets) == len(nums):
                    res.append(subsets.copy())
                    return
                
                if not pick[i]:
                    pick[i] = True
                    subsets.append(nums[i])
                    rec()
                    pick[i] = False
                    subsets.pop()
            
        rec()
        return res