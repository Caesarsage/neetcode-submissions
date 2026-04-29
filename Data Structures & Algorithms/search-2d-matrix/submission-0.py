class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            m = matrix[i]
            start = 0
            end = len(m) - 1
            print(m)

            while start <= end:
                mid = (start + end) // 2

                if m[mid] > target:
                    end = mid - 1
                elif m[mid] < target:
                    start = mid + 1
                else:
                    return True
        return False