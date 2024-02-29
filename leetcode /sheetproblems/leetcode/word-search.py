class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = []
        seta = set()
        def backtrack(idx1,idx2,comp):
            # print(comp)
            if comp == len(word):
                return True
            if (idx1 >= len(board) or idx1 < 0) or (idx2 >= len(board[0]) or idx2 < 0):
                return
            if board[idx1][idx2] != word[comp]:
                return
            if (idx1,idx2) in seta:
                return
            seta.add((idx1,idx2))
            if backtrack(idx1+1,idx2,comp+1):
                return True
            if backtrack(idx1,idx2+1,comp+1):
                return True
            if backtrack(idx1,idx2-1,comp+1):
                return True
            if backtrack(idx1-1,idx2,comp+1):
                return True
            seta.discard((idx1,idx2))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False