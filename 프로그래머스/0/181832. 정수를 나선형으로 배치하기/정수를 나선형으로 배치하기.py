def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    row = 0
    col = 0
    direction = 0
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    for num in range(1, n * n + 1):
        answer[row][col] = num
        
        next_row = row + dr[direction]
        next_col = col + dc[direction]
        
        if (
            next_row < 0
            or next_row >= n
            or next_col < 0
            or next_col >= n
            or answer[next_row][next_col] != 0
        ):
            direction = (direction + 1) % 4
            
        row += dr[direction]
        col += dc[direction]
        
    return answer