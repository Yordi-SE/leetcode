class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.m = ""
        list1 = s.split(' ')
        for k in range(len(list1)):
            for j in list1:
                for i in j:
                    if str(k + 1) == i:
                        self.m += j[:len(j) - 1]
                        if k != len(list1) - 1:
                            self.m += ' '
        return self.m