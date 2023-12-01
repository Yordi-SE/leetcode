class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        for i in range(len(order)):
            index[order[i]] = i

        for j in range(len(words) - 1):
            for i in range(len(words[j])):
                if i < len(words[j]) and i < len(words[j + 1]):
                    if index[words[j][i]] == index[words[j + 1][i]]:
                        continue
                    elif index[words[j][i]] > index[words[j + 1][i]]:
                        return False
                    elif index[words[j][i]] < index[words[j + 1][i]]:
                        break
                elif len(words[j]) > len(words[j + 1]):
                    return False
        return True

