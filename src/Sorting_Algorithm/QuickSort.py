# Revised on 20/05/2025 at 02:56
from numpy.ma.core import equal


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    lesser = [x for x in array[1:] if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array[1:] if x > pivot]

    return quick_sort(lesser) + equal + quick_sort(greater)

test_cases = [
    ([], []),                              # Empty list
    ([42], [42]),                          # Single element
    ([7, 7, 7, 7], [7, 7, 7, 7]),           # Identical elements
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),     # Already sorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),     # Reverse sorted
    ([-3, -1, -7, -5], [-7, -5, -3, -1]),   # Negative numbers
    ([3, -1, 0, -5, 2], [-5, -1, 0, 2, 3]), # Mixed positive and negative
    ([4, 2, 2, 8, 5, 5, 9], [2, 2, 4, 5, 5, 8, 9]),  # Duplicates
    ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6])  # Original test case
]

print("Quick Sort Test Cases:")
for i, (test_case, expected) in enumerate(test_cases, 1):
    result = quick_sort(test_case[:])
    status = "PASS" if result == expected else "FAIL"
    print(f"Test case {i}: {test_case} -> Sorted: {result} | Expected: {expected} | Status: {status}")
