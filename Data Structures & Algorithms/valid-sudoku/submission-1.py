class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        blockset=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                val=board[i][j]
                box=(i//3)*3+(j//3)

                if val in rowset[i] or val in colset[j] or val in blockset[box]:
                    return False
                rowset[i].add(val)
                colset[j].add(val)
                blockset[box].add(val)
        return True