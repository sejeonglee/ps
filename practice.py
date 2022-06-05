def testcase(T):
    inputs = list(map(int, input().split()))

    print(f"Case #{T}: {''.join(answer)}")


def main():
    inputs = list(map(int, input().split()))
    T = inputs[0]
    for i in range(0, T):
        testcase(i + 1)


main()
