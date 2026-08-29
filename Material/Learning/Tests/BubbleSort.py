def bubble_sort(arr: list[int], verbose: bool = False) -> list[int]:
    """
    Sorts a list using Bubble Sort with early-exit optimization.

    Complexity:
        - Time: Best O(n), Average O(n²), Worst O(n²)
        - Space: O(1) auxiliary (In-place)
        - Stability: Stable
    """
    a = arr.copy()
    n = len(a)
    passes = 0
    swaps_total = 0

    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                swaps_total += 1
                if verbose:
                    print(f"  Pass {i+1}, Swap ({a[j+1]} <-> {a[j]}): {a}")
        if not swapped:
            # Early exit: array is already sorted
            break

    if verbose:
        print(f"-> Completed in {passes} passes with {swaps_total} total swaps.")
    return a

# Demonstration
arr_sample = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr_sample)
sorted_arr = bubble_sort(arr_sample, verbose=True)
print("Sorted  :", sorted_arr)
assert sorted(sorted_arr)


