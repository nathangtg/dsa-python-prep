import time
import random

def generate_test_file(filename, n, max_value=1000):
    with open(filename, 'w') as file:
        for _ in range(n):
            file.write(f"{random.randint(1, max_value)}\n")


# ----- Question 1-----
# Implementation of selection sort O(N^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Function to read the whole file and sort O(1)
def read_and_sort(filename, sort_func):
    start_time = time.time()
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file]

    read_time = time.time() - start_time

    # Sort the array
    sort_start = time.time()
    sort_func(arr)
    sort_time = time.time() - sort_start

    total_time = time.time() - start_time

    return {
        "array_size": len(arr),
        "read_time": read_time,
        "sort_time": sort_time,
        "total_time": total_time
    }


# ----- Question 2 -----
# Function to insert a value into a sorted array O(N) * O(N) = O (N^2)
def insert_sorted(sorted_arr, value):
    value = int(value)

    i = 0
    while i < len(sorted_arr) and sorted_arr[i] < value:
        i += 1
    sorted_arr.insert(i, value)


def read_and_insert_sorted(filename):
    start_time = time.time()
    sorted_arr = []

    with open(filename, 'r') as file:
        for line in file:
            value = line.strip()
            insert_sorted(sorted_arr, value)

    total_time = time.time() - start_time

    return {
        "array_size": len(sorted_arr),
        "total_time": total_time
    }


# ----- TESTS -----
def compare_approaches(filename, n=1000):
    generate_test_file(filename, n)

    print("\nApproach 1: Read all then sort")
    result1 = read_and_sort(filename, selection_sort)
    print(f"Array size: {result1['array_size']}")
    print(f"Read time: {result1['read_time']:.6f} seconds")
    print(f"Sort time: {result1['sort_time']:.6f} seconds")
    print(f"Total time: {result1['total_time']:.6f} seconds")

    print("\nApproach 2: Insert into sorted array")
    result2 = read_and_insert_sorted(filename)
    print(f"Array size: {result2['array_size']}")
    print(f"Total time: {result2['total_time']:.6f} seconds")

    print("\nTime Efficiency Comparison:")
    print(f"Approach 1 (Read all, then sort): O(n²) for selection sort")
    print(f"Approach 2 (Insert into sorted array): O(n²) as each insertion is O(n)")

    if result1['total_time'] < result2['total_time']:
        print(f"\nApproach 1 was faster by {result2['total_time'] - result1['total_time']:.6f} seconds")
    else:
        print(f"\nApproach 2 was faster by {result1['total_time'] - result2['total_time']:.6f} seconds")


# Run with different sizes
if __name__ == "__main__":
    filename = "unsorted_values.txt"

    print("Testing with 1,000 values:")
    compare_approaches(filename, 1000)

    print("\n\nTesting with 5,000 values:")
    compare_approaches(filename, 5000)