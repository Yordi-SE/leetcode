class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i, u in enumerate(command):
            if i < len(command) - 1:
                if u == '(' and command[i + 1] == "a":
                    s += "al"
                elif  u == '(' and command[i + 1] == ")":
                    s += "o"
            if u == "G":
                s += u
        return s