class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        def flood(row, col, image, srcColor, newColor, visited):
            row = min( max(0, row), len(image)-1)
            col = min( max(0, col), len(image[0])-1)
            
            if image[row][col] == srcColor and (row, col) not in visited:
                image[row][col] = newColor
                visited.add((row, col))
                flood(row-1, col, image, srcColor, newColor, visited)
                flood(row, col-1, image, srcColor, newColor, visited)
                flood(row+1, col, image, srcColor, newColor, visited)
                flood(row, col+1, image, srcColor, newColor, visited)
            
        visited = set()
        srcColor = image[sr][sc]
        flood(sr, sc, image, srcColor, newColor, visited)
        
        return image