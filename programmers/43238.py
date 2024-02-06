

def test(times, all_time, people):
    n = people
    for time in times: 
        n -= (all_time // time)
        if n <= 0:
            return True
    return False

def solution(n, times):
    answer = 0
    start = 0
    end = 10000000000000-1

    while start <= end :
        mid = (start + end) // 2
        if test(times, mid, n) :
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer


def main():
    times = [1000000000]
    print(solution(1000000000, times))

main()