# Revised on 20/05/2025 02:45
# Minor mistake on J iteration when implementing
def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def test_insertion_sort():
    test_cases = [
        # Test case 1: Already sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),

        # Test case 2: Reverse sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),

        # Test case 3: Random order
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),

        # Test case 4: Single element
        ([42], [42]),

        # Test case 5: Empty list
        ([], []),

        # Test case 6: Duplicates
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),

        # Test case 7: Negative numbers
        ([-3, -1, -4, -2, 0], [-4, -3, -2, -1, 0]),

        # Test case 8: Mixed positive and negative
        ([7, -3, 5, -1, 0, -2], [-3, -2, -1, 0, 5, 7]),
    ]

    passed = True

    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = insertion_sort(input_arr[:])
        if result == expected:
            print(f"Test case {i}: ✅ Passed")
        else:
            print(f"Test case {i}: ❌ Failed (Expected {expected}, Got {result})")
            passed = False

    if passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome tests failed. Please check your implementation.")

test_insertion_sort()
