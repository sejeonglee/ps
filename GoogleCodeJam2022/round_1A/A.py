def testcase(T):
    s = input()
    stack = []
    answer = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
            continue
        if stack[-1] == c:
            stack.append(c)
        elif stack[-1] < c:
            while len(stack) != 0:
                t = stack.pop()
                answer.append(t)
                answer.append(t)
            stack.append(c)
        elif stack[-1] > c:
            while len(stack) != 0:
                t = stack.pop()
                answer.append(t)
            stack.append(c)

    while len(stack) != 0:
        t = stack.pop()
        answer.append(t)

    print(f"Case #{T}: {''.join(answer)}")


def main():
    inputs = list(map(int, input().split()))
    T = inputs[0]
    for i in range(0, T):
        testcase(i + 1)


main()
