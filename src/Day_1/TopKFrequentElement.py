class Solution:
    def TopKFrequentElement(self, numbers: list[int], k: int) -> list[int]:
        frequencies = {}

        for num in numbers:
            frequencies[num] = frequencies.get(num, 0) + 1

        sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

