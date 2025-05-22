# Revised on 20/05//2025
# Minor issue, forgetting to add the base case to the recursion
def merge_sort(array):
    n = len(array)

    if n <= 1:
        return array

    middle = n // 2
    left_half = array[:middle]
    right_half = array[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(l, r):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(l) and right_index < len(r):
        if l[left_index] < r[right_index]:
            result.append(l[left_index])
            left_index += 1
        else:
            result.append(r[right_index])
            right_index += 1

    result.extend(l[left_index:])
    result.extend(r[right_index:])

    return result

if __name__ == "__main__":
    array = [5, 2, 4, 6, 1, 3]
    print("Original array:", array)

    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)

    print("\nTracing merge sort for [5, 2, 4, 1]:")
    print("1. Split into [5, 2] and [4, 1]")
    print("2. Split [5, 2] into [5] and [2]")
    print("3. Merge [5] and [2] into [2, 5]")
    print("4. Split [4, 1] into [4] and [1]")
    print("5. Merge [4] and [1] into [1, 4]")
    print("6. Merge [2, 5] and [1, 4] into [1, 2, 4, 5]")

