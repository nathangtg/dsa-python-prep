class Solution:
    def TopKFrequentElement(self, numbers: list[int], k: int) -> list[int]:
        frequencies = {}

        for num in numbers:
            frequencies[num] = frequencies.get(num, 0) + 1

        bucket = [[] for _ in range(len(frequencies) +1)]

        answer = []

        for num, freq in frequencies:
            bucket[freq].append(num)

        for i in range(len(bucket) -1, 0, -1):
            for num in bucket:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return [0,0]