class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        
        # find the row where target could be using binary search
        # on last and first element of a row
        top, bottom = 0, rows-1
        while(top<=bottom):
            row = (top+bottom)//2
            # compare last element of the row
            if target > matrix[row][-1]:
                top = row+1
            # compare first element of the row
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                # target is between [row][0] and [row][-1]
                break
        # target row was not found 
        # eg top is [row][0] and bottom is [row-1][-1]
        if top > bottom:
            return False

        # find the exact target using binary search on 
        # the particular row
        l, r = 0, cols-1
        row = (top+bottom)//2
        while(l<=r):
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m-1
            elif target > matrix[row][m]:
                l = m+1
            else: 
                return True
        return False
