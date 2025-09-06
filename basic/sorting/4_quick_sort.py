# Implement Merge Sort and return intermediate states.
# If two pairs have the same key, maintain their original relative order.

from typing import List, Tuple

class Solution:
    def QuickSort(self, pairs: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
        states = [pairs.copy()]

        def partition(arr: List[Tuple[int, str]], low: int, high: int) -> int:
            pivot = arr[high][0]  # choose the last element as pivot
            print("pivot:", pivot)
            i = low - 1

            for j in range(low, high):
                if arr[j][0] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            states.append(arr.copy())  # record state after partition
            return i + 1

        def sort(arr: List[Tuple[int, str]], low: int, high: int):
            if low < high:
                pi = partition(arr, low, high)
                sort(arr, low, pi - 1)   # recursively sort left
                sort(arr, pi + 1, high)  # recursively sort right

        sort(pairs, 0, len(pairs) - 1)
        return states


def test():
    #pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
    pairs = [(3, "cat"),  (5, "bear"), (3, "bird"), (4, "fox"), (2, "dog")]
    result = Solution().QuickSort(pairs)
    for step in result:
        print(step)

if __name__ == "__main__":
    test()