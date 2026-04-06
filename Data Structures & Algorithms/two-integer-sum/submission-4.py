class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ss = {}
        for i, n in enumerate(nums):
            if n in ss:
                ss[n].append(i)
            else:
                ss[n] = [i]
        print(ss)
        for i, n in enumerate(nums):
            if target - n in nums:
                if n == target - n:
                    if len(ss[n]) > 1:
                        return [i, ss[n][1]]
                    else:
                        continue
                return [i, ss[target-n][0]]
        