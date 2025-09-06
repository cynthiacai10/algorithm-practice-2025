"""
Delft Algorithm Programming Contest 2024
E - Expected Error
https://open.kattis.com/problems/expectederror

Cynthia
September 6, 2025
"""

def main():
    n, k, p = map(int, input().split())

    # not converting probability to %
    # But ALLL * 100!!!! to avoid float number

    # compute time: continue, backspace, restart
    t_cont_corr = (n-k) + 1 # type, submit
    t_cont_wrong = t_cont_corr + 3 + n + 1
    t_cont = t_cont_corr * (100-p) + t_cont_wrong * p

    t_back_wrong = 1 + (n-k) + 1 # backspace, type, submit
    t_back_corr = t_back_wrong + 3 + n + 1
    t_back = t_back_corr * (100-p) + t_back_wrong * p

    t_restart = 100 * (3 + n + 1) # delete all, type, submit

    if t_cont < t_back and t_cont < t_restart:
        print("continue")
        return
    if t_back < t_cont and t_back < t_restart:
        print("backspace")
    if t_restart < t_back and t_restart < t_cont:
        print("restart")


if __name__ == "__main__":
    main()