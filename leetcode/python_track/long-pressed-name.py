class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first = 0
        if len(name) > len(typed):
            return False

        second = 0
        while first < len(name):
            if name[first] != typed[second]:
                return False
            checke = typed[second]
            second += 1
            first += 1
            while (first < len(name) and second < len(typed)) and typed[second - 1] == typed[second] and name[first] != name[first-1]:
                second += 1
            if first >= len(name):
                while second < len(typed):
                    if typed[second] != checke:
                        return False
                    second += 1
            if second >=len(typed) and first<len(name):
                return False
        return True