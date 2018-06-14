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