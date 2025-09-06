# Implement Merge Sort and return intermediate states.
# If two pairs have the same key, maintain their original relative order.

from typing import List, Tuple

class Solution:
    def MergeSort(self, pairs: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
        states = [pairs.copy()]

        def merge(left: List[Tuple[int, str]], right: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
            merged = []
            i = j = 0

            # Merge while preserving stability
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Add remaining elements
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        def sort(arr: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
            # splits, recursively sorts each half, and merges them.
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])

            merged = merge(left, right)
            states.append(merged.copy())

            return merged

        sort(pairs)
        return states

def test():
    #pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
    pairs = [(3, "cat"),  (5, "bear"), (3, "bird"), (4, "fox"), (2, "dog")]
    result = Solution().MergeSort(pairs)
    for step in result:
        print(step)

if __name__ == "__main__":
    test()