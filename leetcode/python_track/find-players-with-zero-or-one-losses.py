class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser = {}
        winner = {}
        answer = [[], []]
        for i in matches:
            if i[1] in looser.keys():
                looser[i[1]] += 1
            elif i[1] not in looser.keys():
                looser[i[1]] = 1
            if i[0] not in looser.keys():
                looser[i[0]] = 0
        print(looser)
        for i in looser.keys():
            if looser[i] == 1:
                answer[1].append(i)
            elif looser[i] == 0:
                answer[0].append(i)
        # for i in winner.keys():
        #     answer[0].append(i)
        # for i in looser.keys():
            
        # for i in looser.keys():
        #     answer[1].append(i)
        answer[0].sort()
        answer[1].sort()
        return answer