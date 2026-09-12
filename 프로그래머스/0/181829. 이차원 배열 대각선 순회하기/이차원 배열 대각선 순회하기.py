def solution(board, k):
    result = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                result += board[i][j]
    
    return result
                
    # result = [board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k]
    # return sum(result)