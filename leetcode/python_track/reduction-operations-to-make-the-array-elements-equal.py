class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        set1 = list(set(nums))
        set1.sort(reverse=True)
        counter = Counter(nums)
        for i in range(1,len(set1) - 1):
            counter[set1[i]] += counter[set1[i - 1]]
        operation = 0
        for i in range(len(set1) - 1):
            operation += counter[set1[i]]
        # print(counter)
        return operation