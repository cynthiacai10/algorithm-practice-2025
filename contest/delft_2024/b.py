"""
Delft Algorithm Programming Contest 2024
B - Battle Of Nieuwpoort
https://open.kattis.com/problems/battleofnieuwpoort

Cynthia
September 6, 2025
"""

alpha = "abcdefg"


def convert_base(num: int, base: int) -> str:
    # Algorithm explained by my friend ej200CE
    res = ""
    weight = base
    while num > 0:
        digit = num % weight
        digit = str(digit) if digit < 10 else alpha[digit-10]
        res += digit
        num = num // weight
    return res[::-1]


def main():
    line = input().split()
    num = int(line[0])
    if num % 100 == 0:
        print(10, num)
        return
    
    for base in range(16, 1, -1):
        num_base = convert_base(num, base)
        if num_base[-2:] == "00":
            print(base, num_base)
            return
    print("impossible")


if __name__ == "__main__":
    main()