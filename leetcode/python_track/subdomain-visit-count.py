class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for i, u in enumerate(cpdomains):
            count_and_domain = u.split(" ")
            subdomains = count_and_domain[1].split(".")
            subdomains.reverse()
            for i in range(len(subdomains)):
                s = ".".join(list(reversed(subdomains[:i + 1])))
                if s in hashmap.keys():
                    hashmap[s] += int(count_and_domain[0])
                else:
                    hashmap[s] = int(count_and_domain[0])
        res = []
        for i in hashmap.keys():
            res.append(str(hashmap[i]) + " " + i)
        return res