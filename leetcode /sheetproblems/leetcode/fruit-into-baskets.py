class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        x = 0
        y = 0
        hashmap = {}
        Len = 0
        while y < len(fruits):
            if fruits[y] not in hashmap.keys():
                if len(hashmap.values()) == 2:
                    x = min(hashmap.values()) + 1
                    for key, value in hashmap.items():
                        if value == min(hashmap.values()):
                            del hashmap[key]
                            break 
            if Len < (y - x + 1):
                Len = (y - x + 1)            
            hashmap[fruits[y]] = y
            y += 1
        return Len