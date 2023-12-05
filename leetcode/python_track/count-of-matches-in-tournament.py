class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n # initial number of teams
        matches = 0
        while teams > 1:
            if teams % 2 == 0:
                matches += (teams // 2)
                teams = teams // 2
            elif teams % 2:
                matches += (teams // 2)
                teams = (teams // 2) + 1
        return matches
