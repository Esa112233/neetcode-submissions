class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        out_l, out_r = 0, len(matrix) - 1

        start_index = -1

        while out_l <= out_r:

            middle =  (out_r + out_l)//2

            

            if matrix[middle][0] == target or matrix[middle][-1] == target:
                return True

            if target > matrix[middle][0] and target < matrix[middle][-1]:
                start_index = middle
                break

            if target > matrix[middle][-1]:
                out_l = middle + 1
            if target < matrix[middle][0]:
                out_r = middle - 1
        
        if out_r < out_l:
            return False

        if start_index == -1:
            return False
        
        new_mat = matrix[start_index]
        in_l, in_r = 0, len(new_mat) - 1

        while in_l <= in_r:

            middle = (in_r + in_l)//2

            if new_mat[middle] == target:
                return True
            elif new_mat[middle] < target:
                in_l = middle + 1
            elif new_mat[middle] > target:
                in_r = middle - 1
        
        return False

                    

            