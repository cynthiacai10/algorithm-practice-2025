"""
Codeforces
1138a. Sushi for two
https://codeforces.com/problemset/problem/1138/A

Yudanya
August 5th, 2025
"""

def sushi_for_two(sushi):
    # value: 1, 2
    # return the length of the longest subarray that is half 1, half 2
    if len(sushi) < 2:
        return 0
    
    prev_count = 0 # no previous group yet
    count = 1 # current group size
    max_size = 0

    # Group the sushi into consecutive same elements
    for i in range(1, len(sushi)):
        if sushi[i] != sushi[i-1]:
            # switch point: process group
            max_size = max(max_size, 2*min(count, prev_count))
            prev_count = count
            count = 1 # restart the count
        else:
            count += 1
    
    # process the final group pair
    max_size = max(max_size, 2 * min(prev_count, count))
    
    return max_size


def test():
    test_set = [[7, "2 2 2 1 1 2 2"],
                [6, "1 2 1 2 1 2"],
                [9, "2 2 1 1 1 2 2 2 2"],
                [8, "1 1 2 2 1 1 2 2"],
                [2, "1 2"], # output: 2
                [1, "2"]
                ]
    for length, sushi in test_set:
        sushi_lst = list(map(int, sushi.split()))
    
        if length != len(sushi_lst):
            print("Input eroor")
            return 0
            
        print("Input sushi:", sushi_lst)
        res = sushi_for_two(sushi_lst)
        print("Result:",res)


def main():
    length = int(input())
    sushi_lst = list(map(int, input().split()))
    print(sushi_for_two(sushi_lst))


if __name__ == "__main__":
    main()