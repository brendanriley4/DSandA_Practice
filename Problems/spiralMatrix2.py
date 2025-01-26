from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper = 0
        lower = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0
        direction = 0
        output = []
        curr_coords = [0, 0]
        output.append(matrix[curr_coords[0]][curr_coords[1]])

        while len(output) != (len(matrix) * len(matrix[0])):
            if direction == 0:
                if curr_coords[1] + 1 <= right:
                    curr_coords[1] += 1
                    output.append(matrix[curr_coords[0]][curr_coords[1]])
                else:
                    curr_coords[1] -= 1
                    right -= 1
                    direction = 1
            elif direction == 1:
                if curr_coords[0] + 1 <= lower:
                    curr_coords[0] += 1
                    output.append(matrix[curr_coords[0]][curr_coords[1]])
                else:
                    curr_coords[0] -= 1
                    lower -= 1
                    direction = 2
            elif direction == 2:
                if curr_coords[1] - 1 >= left:
                    curr_coords[1] -= 1
                    output.append(matrix[curr_coords[0]][curr_coords[1]])
                else:
                    curr_coords[0] += 1
                    left += 1
                    direction = 3
            elif direction == 3:
                if curr_coords[0] - 1 >= upper:
                    curr_coords[0] -= 1
                    output.append(matrix[curr_coords[0]][curr_coords[1]])
                else:
                    curr_coords[0] += 1
                    upper += 1
                    direction = 0

        return output