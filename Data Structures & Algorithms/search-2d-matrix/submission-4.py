class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        while l <len(matrix) and l <= r:
            mid = (l+r)//2
            # print(l, r, mid)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        if matrix[mid][0] > target:
            mid -= 1
        
        fixi = mid
        l = 0
        r = len(matrix[0])

        while l < len(matrix[0]) and l <= r:
            mid = (l+r)//2

            if matrix[fixi][mid] == target:
                return True
            if matrix[fixi][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False