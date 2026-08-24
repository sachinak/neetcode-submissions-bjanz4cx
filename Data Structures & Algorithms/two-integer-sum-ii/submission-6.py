class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le = len(numbers)
        for idx, n in enumerate(numbers):
            t = target - n
            lo = idx+1
            hi = le-1
            
            while lo <= hi:
                 
                mid = (lo+hi)//2
                
                if t == numbers[mid]:
                    return [idx+1, mid+1]
                if t > numbers[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
            
        return [0,1 ]
