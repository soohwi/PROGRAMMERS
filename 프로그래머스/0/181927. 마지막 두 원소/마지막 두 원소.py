def solution(num_list):
    last_num = num_list[-1]
    prev_last_num = num_list[-2]
    
    if last_num > prev_last_num:
        num_list.append(last_num - prev_last_num)
    else:
        num_list.append(last_num * 2)
        
    return num_list