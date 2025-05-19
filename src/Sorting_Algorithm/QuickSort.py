def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

# Example usage
if __name__ == "__main__":
    # Test with our example array
    arr = [5, 2, 4, 6, 1, 3]
    print("Original array:", arr)

    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

    # Let's trace a simple example
    print("\nTracing quicksort for [5, 2, 4, 6, 1, 3]:")
    print("1. Choose pivot = 3 (last element)")
    print("2. After first partition: [2, 1, 3, 6, 4, 5]")
    print("   - Elements <= 3: [2, 1]")
    print("   - Pivot (3) is at its final position")
    print("   - Elements > 3: [6, 4, 5]")
    print("3. Recursively sort left part [2, 1]")
    print("   - Choose pivot = 1")
    print("   - After partition: [1, 2]")
    print("4. Recursively sort right part [6, 4, 5]")
    print("   - Choose pivot = 5")
    print("   - After partition: [4, 5, 6]")
    print("5. Final sorted array: [1, 2, 3, 4, 5, 6]")
