def heap_sort(arr):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


def test_heap_sort():
    test_cases = [
        # Test case 1: Already sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),

        # Test case 2: Reverse sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),

        # Test case 3: Random values
        ([4, 10, 3, 5, 1], [1, 3, 4, 5, 10]),

        # Test case 4: Single element
        ([42], [42]),

        # Test case 5: Empty list
        ([], []),

        # Test case 6: All elements are equal
        ([7, 7, 7, 7], [7, 7, 7, 7]),

        # Test case 7: With duplicates
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),

        # Test case 8: Negative numbers
        ([-3, -1, -4, -2, 0], [-4, -3, -2, -1, 0]),

        # Test case 9: Mixed negatives and positives
        ([7, -3, 5, -1, 0, -2], [-3, -2, -1, 0, 5, 7]),
    ]

    passed = True

    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = heap_sort(input_arr[:])
        if result == expected:
            print(f"Test case {i}: ✅ Passed")
        else:
            print(f"Test case {i}: ❌ Failed (Expected {expected}, Got {result})")
            passed = False

    if passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome test cases failed. Please debug the implementation.")

test_heap_sort()
