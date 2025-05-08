class Solution:
    def intersectionOfArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return list(set(arr1).intersection(set(arr2)))