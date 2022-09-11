# https://www.acmicpc.net/problem/4375


def solve(n):
    if n == 0:
        print(0)
        return

    seq_of_1 = 1
    length = 1
    while True:
        remainder = seq_of_1 % n

        if remainder == 0:
            print(length)
            return

        seq_of_1 = (seq_of_1 * 10 + 1) % n
        length += 1


def main():
    while True:
        try:
            s = input()
            solve(int(s))
        except EOFError:
            return
        except KeyboardInterrupt:
            return


main()
