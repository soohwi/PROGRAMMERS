def solution(arr):
    x = 0
    
    while True:
        new_arr = []
        
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new_arr.append(i // 2)
            elif i < 50 and i % 2 != 0:
                new_arr.append(i * 2 + 1)
            else: 
                new_arr.append(i)
                
        if new_arr == arr:
            break
        
        arr = new_arr
        x += 1
    
    return x