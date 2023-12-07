class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = 0
        answer = []
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operations += abs(i - j)
            answer.append(operations)
            operations = 0
        return answer