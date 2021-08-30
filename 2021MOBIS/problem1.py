import itertools

input_dice = [[1,1,1,1,1,1]]

def ordered_check_number(check_dict, dice_ordered, n):
    check_dict[n] = True

    if len(dice_ordered) == 0:
        return
    
    dice = dice_ordered[0]
    next_dice_ordered = dice_ordered[1:]
    
    for plane in dice:
        next_n = n * 10 + plane
        ordered_check_number(check_dict, next_dice_ordered, next_n)
        
        
        

def solution(dices):
    check_dict = dict()
    answer = 1
    
    for dice_ordered in itertools.permutations(dices):
        ordered_check_number(check_dict, dice_ordered, 0)

    s = set(check_dict.keys())

    for i in range(1, 10000):
        if i not in s:
            answer = i
            break

    return answer

print(solution(input_dice))