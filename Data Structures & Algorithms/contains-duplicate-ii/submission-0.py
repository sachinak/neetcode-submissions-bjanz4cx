class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arr = [[v,i] for i,v in enumerate(nums)]
        arr.sort()
        for i in range(1, len(nums)):
            if arr[i][0] == arr[i-1][0]:
                if arr[i][1] - arr[i-1][1] <= k:
                    return True
        return False