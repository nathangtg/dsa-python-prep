# Revised on 20/05/2025 at 02:52
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test cases and expected outputs
test_cases = [
    ([], []),                              # Empty list
    ([42], [42]),                          # Single element
    ([7, 7, 7, 7], [7, 7, 7, 7]),           # Identical elements
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),     # Already sorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),     # Reverse sorted
    ([-3, -1, -7, -5], [-7, -5, -3, -1]),   # Negative numbers
    ([3, -1, 0, -5, 2], [-5, -1, 0, 2, 3]), # Mixed positive and negative
    ([4, 2, 2, 8, 5, 5, 9], [2, 2, 4, 5, 5, 8, 9]),  # Duplicates
    ([23, 16, 37, 43, 2, 41, 38], [2, 16, 23, 37, 38, 41, 43])  # Original test case
]

# Execute test cases
for i, (test_case, expected) in enumerate(test_cases, 1):
    result = selection_sort(test_case[:])
    status = "PASS" if result == expected else "FAIL"
    print(f"Test case {i}: {test_case} -> Sorted: {result} | Expected: {expected} | Status: {status}")