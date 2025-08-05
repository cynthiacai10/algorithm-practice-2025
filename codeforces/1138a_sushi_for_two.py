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
    
    curr_left = 1 # 1 or 2
    curr_left_count, prev_left_count = 0, 0
  
    max_size = 0

    for i in range(0, len(sushi)): # the break        
        # track the length of left part
        if sushi[i] != curr_left or i == len(sushi)-1: # switching point
            # count the size
            size = 2 * min(prev_left_count, curr_left_count)
            max_size = max(size, max_size)

            # move on, restart counting
            curr_left = sushi[i]
            prev_left_count = curr_left_count
            curr_left_count = 1
        else:
            # continue counting
            curr_left_count += 1
    
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
        sushi_lst = list(map(int, sushi))
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
    test()
