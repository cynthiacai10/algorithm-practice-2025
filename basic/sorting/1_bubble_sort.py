# Implement Bubble Sort and return intermediate states.
# If two pairs have the same key, maintain their original relative order.

from typing import List, Tuple

class Solution:
    def BubbleSort(self, pairs: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
        n = len(pairs)
        states = [pairs.copy()]
        for i in range(n-1):
            for j in range(n-i-1):
                if pairs[j][0] > pairs[j+1][0]:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
            states.append(pairs.copy())
        return states

def test():
    #pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
    pairs = [(3, "cat"),  (5, "bear"), (3, "bird"), (4, "fox"), (2, "dog")]
    result = Solution().BubbleSort(pairs)
    for step in result:
        print(step)

if __name__ == "__main__":
    test()