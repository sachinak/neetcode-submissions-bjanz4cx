class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = 1

        while numbers[l] < target/2:
            t = target - numbers[l]
            if t in numbers[l+1:]:
                return [l+1, l+2+numbers[l+1:].index(t)]
            l+=1
        
            