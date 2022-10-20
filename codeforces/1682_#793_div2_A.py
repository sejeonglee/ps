"""https://codeforces.com/contest/1682/problem/A
"""


def solve():
    answer: int = 0

    n: int = int(input())
    s: str = input()

    center_pos: int = int(n / 2)
    center_char: str = s[center_pos]

    for c in reversed(s[0:center_pos]):
        if c == center_char:
            answer += 2
        else:
            break
    if n % 2 == 1:
        answer += 1

    return answer


def main():
    T = int(input())
    for i in range(0, T):
        print(f"{solve()}")


main()
