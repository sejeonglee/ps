
#런타임에러 + 초과
input_a = ["abab","bbaa","bababa","bbbabababbbaa","bbabb"]

memo = {"a":True, "": False}

def try_rule_a(s):
    if s in memo:
        return memo[s]

    if s[0]=="a":
        ret = try_rule_a(s[1:]) or try_rule_b(s[1:])
        memo[s] = ret
        return ret
    elif s[-1]=="a":
        ret = try_rule_a(s[:-1]) or try_rule_b(s[:-1])
        memo[s] = ret
        return ret
    else:
        return False



def try_rule_b(s):
    def count_a(s):
        count = 0
        for c  in s:
            if c == "a":
                count = count+1
        return count
        
    if s in memo:
        return memo[s]
    
    for i in range(int(len(s)/2), 0, -1):
        if (count_a(s[i:-i]) == i) and(s[0:i] == ("b"*i)) and (s[-i:]==("b"*i)):
            ret = try_rule_a(s[i:-i]) or try_rule_b(s[i:-i])
            memo[s] = ret
            return ret
    return False


def solution(a):
    answer = []

    for s in a:
        answer.append(try_rule_a(s) or try_rule_b(s))

    return answer


print(solution(input_a))