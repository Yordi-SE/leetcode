class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target-1
        moves = 0
        while maxDoubles > 0 and target > 1:
            moves += (1 + (target % 2))
            target = target //2
            maxDoubles -= 1
        # print(target)
        return moves + (target - 1)