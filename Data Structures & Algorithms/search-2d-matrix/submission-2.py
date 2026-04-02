class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        high = ROWS - 1
        target_row = None
        while low <= high:
            mid = low + ((high-low)//2)
            if matrix[mid][0] > target and matrix[mid][COLS-1] < target:
                target_row = mid
                break
            if matrix[mid][COLS-1] < target:
                low = mid + 1
            else:
                high = mid - 1
        if not target_row:
            target_row = low
        if target_row >= ROWS:
            return False
        low = 0
        high = COLS - 1
        while low <= high:
            mid = low + ((high-low)//2)
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False