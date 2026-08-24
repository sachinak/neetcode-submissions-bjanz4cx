class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            

            for jdx in range(idx+1,len(nums)):
                if jdx > idx+1 and nums[jdx-1] == nums[jdx]:
                    continue
                
                l = jdx+1
                r = len(nums) - 1
                
                while l < r:
                    t = nums[idx] + nums[jdx]+nums[l]+nums[r]
                    if t == target:
                        res.append([nums[idx], nums[jdx], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                        while l < r and nums[r] == nums[r+1]:
                            r-=1
                    elif t > target:
                        r-=1
                    else:
                        l+=1
        return res