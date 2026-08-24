class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, v in enumerate(nums):
            if v > 0:
                break
            if idx> 0 and v == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                t = nums[idx] + nums[l] + nums[r]
                if t == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif t > 0:
                    r-=1
                else:
                    l+=1
        return res