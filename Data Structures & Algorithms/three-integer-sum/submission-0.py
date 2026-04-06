class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []
        for i in range(n-2):
            for j in range(i+1, n-1):
                t = -(nums[i] + nums[j])
                if t in nums[j+1:]:
                    temp = [nums[i], nums[j], t]
                    if temp not in res:
                        res.append(temp)
        return res