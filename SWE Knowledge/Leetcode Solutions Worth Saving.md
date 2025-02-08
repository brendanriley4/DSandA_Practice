Binary search of 2D array:
```python
class Solution:  
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        if not matrix or not matrix[0]:  
            return False  
  
        rows, cols = len(matrix), len(matrix[0])  
        l, r = 0, rows * cols - 1  
  
        while l <= r:  
            m = l + (r - l) //2  
  
	        # To think of a 2D matrix flattened, the way we would get row and                  # column would be  
            # row = how many rows before this are full? - integer division                     # column = how many spots are filled after that is done - modulus      
            row = m // cols  
            col = m % cols  
  
            if matrix[row][col] == target:  
                return True  
            elif matrix[row][col] < target:  
                l = m + 1  
            else:  
                r = m - 1  
  
        return False
```

Merge-Sort on linked list:
	-merge sort just means break into smaller and smaller sorted lists and then combine them to make big sorted list
	
