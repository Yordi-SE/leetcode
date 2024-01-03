class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        l = 0
        res = []
        for i in range(0,len(tasks), 4):
            res.append(max(processorTime[l] + tasks[i],processorTime[l] + tasks[i + 1],processorTime[l] + tasks[i + 2], processorTime[l] + tasks[i + 3]))
            l += 1
        return (max(res))