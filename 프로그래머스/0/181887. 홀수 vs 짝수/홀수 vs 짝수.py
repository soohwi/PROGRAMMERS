def solution(num_list):
    
    odd = sum(num_list[::2])
    even = sum(num_list[1::2])
    
    return odd if even == odd else max(even, odd)