# Source: Neetcode
# Implement Insertion Sort and return intermediate states.
# If two pairs have the same key, maintain their original relative order.

from typing import List, Tuple

class Solution:
    def insertionSort(self, pairs: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
        n = len(pairs)
        states = []
        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j][0] > pairs[j + 1][0]:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            states.append(pairs.copy())
        return states

def test():
    #pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
    pairs = [(3, "cat"),  (5, "bear"), (3, "bird"), (2, "dog"), (4, "fox")]
    result = Solution().insertionSort(pairs)
    for step in result:
        print(step)

if __name__ == "__main__":
    test()