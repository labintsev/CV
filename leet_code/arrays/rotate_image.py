from typing import List


class Solution:
    def rotate_transpose(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        for i in range(1, n):
            for j in range(0, n-1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        n = len(m) - 1
        for j in range(len(m)//2):
            for i in range(n):
                m[i+j][j], m[j][n-j-i], m[n-j][n-j-i], m[n-j][i+j] = m[n-j][i+j], m[i+j][j], m[j][n-j-i], m[n-j][n-j-i]





matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

if __name__ == '__main__':
    s = Solution()
    s.rotate(matrix)
    print(matrix)
    # assert nums == [3, 4, 5, 1, 2]