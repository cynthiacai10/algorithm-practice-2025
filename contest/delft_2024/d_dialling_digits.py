"""
Delft Algorithm Programming Contest 2024
D - Dialling Digits
https://open.kattis.com/problems/diallingdigits

Cynthia
September 6, 2025
"""

ch_mapping = {
    "2": {"a", "b", "c"},
    "3": {"d", "e", "f"},
    "4": {"g", "h", "i"},
    "5": {"j", "k", "l"},
    "6": {"m", "n", "o"},
    "7": {"p", "q", "r", "s"},
    "8": {"t", "u", "v"},
    "9": {"w", "x", "y", "z"}
}


def word_to_num(word):
    res = ""
    for ch in word:
        for num, char_set in ch_mapping.items():
            if ch in char_set:
                res += num
                break
    return int(res)


def main():
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]
    nums = [int(input()) for _ in range(m)]

    dict = {} # num -> list of words
    for num in nums:
        dict[num] = []

    for word in words:
        new_num = word_to_num(word)
        if new_num in dict:
            dict[new_num].append(word)

    for num in nums:
        all_words = dict[num]
        print(len(all_words), " ".join(all_words))


if __name__ == "__main__":
    main()