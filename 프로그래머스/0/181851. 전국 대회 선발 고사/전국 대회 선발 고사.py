def solution(rank, attendance):
    newRank = []
    for idx, (r, a) in enumerate(zip(rank, attendance)):
        if a:
            newRank.append((idx, r))
    top3 = sorted(newRank, key=lambda x: x[1])
    
    return 10000*top3[0][0] + 100*top3[1][0] + top3[2][0]
        