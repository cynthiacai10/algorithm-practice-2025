#  Sorting Algorithms

## 1. Bubble Sort
How it works: Repeatedly swaps adjacent elements if they are in the wrong order.

Time Complexity:
- Best: O(n) (already sorted)
- Average: O(n²)
- Worst: O(n²)

Space Complexity: O(1) (in-place)

Stability: Yes

Use Cases: Educational purposes, small datasets; rarely used in practice.

## 2. Insertion Sort
How it works: Builds the sorted array one element at a time by inserting elements into their correct position.

Time Complexity:
- Best: O(n) (already sorted)
- Average: O(n²)
- Worst: O(n²)

Space Complexity: O(1)

Stability: Yes

Use Cases: Small or nearly-sorted arrays; often used as a subroutine in hybrid algorithms.

## 3. Selection Sort
How it works: Repeatedly selects the smallest (or largest) element and moves it to its final position.

Time Complexity: O(n²) for all cases

Space Complexity: O(1)

Stability: No (can be made stable with extra effort)

Use Cases: Simple to implement; rarely used in practice.

## 4. Merge Sort
How it works: Divide-and-conquer: splits the array, sorts halves recursively, then merges them.

Time Complexity: O(n log n) for all cases

Space Complexity: O(n) (needs extra array for merging)

Stability: Yes

Use Cases: Large datasets; guaranteed O(n log n); stable sorting required.

## 5. Quick Sort
How it works: Divide-and-conquer: chooses a pivot, partitions the array, and recursively sorts partitions.

Time Complexity:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²) (depends on pivot choice)

Space Complexity: O(log n) average (recursion stack)

Stability: No

Use Cases: Very fast in practice; standard choice for general-purpose sorting.

## 6. Heap Sort
How it works: Builds a heap and repeatedly extracts the maximum (or minimum).

Time Complexity: O(n log n) in all cases

Space Complexity: O(1) (in-place)

Stability: No

Use Cases: Large datasets when O(n log n) worst-case is required and space is limited.

## 7. TimSort
How it works: Hybrid of Merge Sort and Insertion Sort; exploits existing runs in data.

Time Complexity:
- Best: O(n)
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity: O(n)

Stability: Yes

Use Cases: Used in Python (list.sort()) and Java (Arrays.sort() for objects); excellent for real-world data.