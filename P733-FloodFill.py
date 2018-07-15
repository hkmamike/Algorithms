class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        def flood(row, col, image, srcColor):
            row = min( max(0, row), len(image)-1)
            col = min( max(0, col), len(image[0])-1)
            
            if image[row][col] == srcColor:
                image[row][col] = -1
                flood(row-1, col, image, srcColor)
                flood(row, col-1, image, srcColor)
                flood(row+1, col, image, srcColor)
                flood(row, col+1, image, srcColor)
            
        def replaceChanged(image, newColor):
            H = len(image)
            W = len(image[0])
            
            for r in range(H):
                for c in range(W):
                    if image[r][c] == -1:
                        image[r][c] = newColor
            
        srcColor = image[sr][sc]
        flood(sr, sc, image, srcColor)
        replaceChanged(image, newColor)
        
        return image
        