class Solution:
    def validlst(self,lst):
        digits=[x for x in lst if x!='.']
        return len(digits)==len(set(digits))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row checking
        for i in range(9):
            if not self.validlst(board[i]):
                return False
        # column checking 
        for i in range(9):
            lst=[]
            for j in range(9):
                lst.append(board[j][i])
            if not self.validlst(lst):
                return False
        # check block
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=[]
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        box.append(board[r][c])
                if not self.validlst(box):
                    return False
        return True

        


        