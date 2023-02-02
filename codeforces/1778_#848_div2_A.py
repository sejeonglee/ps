from array import array


def solve():
    n = int(input())
    a = array("b", map(int, input().split()))

    sum_of_arr = sum(a)

    flipped_results = []
    for i, v in enumerate(a):
        if i == 0:
            continue
        flipped_sub_result = -a[i] - a[i - 1]
        flipped_results.append(flipped_sub_result)

    answer = sum_of_arr + 2 * max(flipped_results)

    return answer


def main():
    T = int(input())
    for i in range(0, T):
        print(f"{solve()}")


main()
