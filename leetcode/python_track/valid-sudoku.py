class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            checker1 = set()
            checker2 = set()
            for j in range(len(board)):
                if board[i][j] == "." and board[j][i] == ".":
                    continue
                elif board[i][j] != "." and int(board[i][j]) in checker1:
                    return False
                elif board[j][i] != "." and int(board[j][i]) in checker2:
                    return False
                elif board[j][i] == ".":
                    checker1.add(int(board[i][j]))
                elif board[i][j] == ".":
                    checker2.add(int(board[j][i]))
                else:
                    checker2.add(int(board[j][i]))
                    checker1.add(int(board[i][j]))
            checker3 = set()
            for i in range(0,len(board), 3):
                res = []
                for j in range(0, len(board), 3):
                    res += board[j][i:i + 3] + board[j + 1][i:i + 3] + board[j + 2][i:i + 3]
                    for k in range(len(res)):
                        if res[k] != '.':
                            if res[k] in checker3:
                                return False
                            else:
                                checker3.add(res[k])
                    checker3 = set()
                    res = []
        return True