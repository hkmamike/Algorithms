## Cleaner Solution
class Solution:
    def bSearchY(self, matrix, target):
            up = 0
            down = len(matrix)-1
            while up < down:
                mid = (down + up) // 2
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][-1] < target:
                    up = mid + 1
                else:
                    down = mid
            return up
    def bSearchX(self, matrix, target, Y):
        L = 0
        R = len(matrix[Y])-1
        while L < R:
            M = (L+R) // 2
            if matrix[Y][M] == target:
                return M
            elif matrix[Y][M] < target:
                L = M + 1
            else:
                R = M
        return L
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = self.bSearchY(matrix, target)
        C = self.bSearchX(matrix, target, R)
        return target == matrix[R][C]

class Solution:
    def searchMatrix(self, matrix, target):
        height = len(matrix)
        
        if height == 0:
            return False
        
        width = len(matrix[0])
        
        if width == 0:
            return False
        
        
        if target < matrix[0][0]:
            return False
        elif target > matrix[height-1][width-1]:
            return False
        
        def binSearchY (matrix, target):
            up = 0
            down = len(matrix) - 1
            
            while down > up:
                mid = (up + down) // 2
                
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][-1] < target:
                    up = mid+1
                else:
                    down = mid
                    
            return up
            
        def binSearchX (array, target):
            left = 0
            right = width-1
            
            while left < right:
                mid = (left + right) // 2
                
                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    right = mid
                else:
                    left = mid + 1
                    
            return array[left] == target
            
        r = binSearchY(matrix, target)
        found = binSearchX(matrix[r], target)
        
        return found