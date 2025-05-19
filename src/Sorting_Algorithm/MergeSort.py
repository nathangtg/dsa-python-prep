def merge_sort(array):
    if len(array)  <= 1:
        return array

    middle = len(array) // 2
    lh = array[:middle]
    rh = array[middle:]

    lh = merge_sort(lh)
    rh = merge_sort(rh)

    return merge(lh, rh)

def merge(l, r):
    result = []
    li = 0
    ri = 0

    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            result.append(l[li])
            li += 1
        else:
            result.append(r[ri])
            ri += 1

    result.extend(l[li:])
    result.extend(r[ri:])

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

