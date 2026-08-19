def solution(a, b, c, d):
    l = sorted([a, b, c, d])
    
    # 리스트에서 서로 다른 숫자들 (중복 제거)
    unique = sorted(set(l))
    
    if len(unique) == 1:
        # 다 같음: [4]
        p = unique[0]
        return 1111 * p
    
    elif len(unique) == 4:
        # 다 다름: [1,1,1,1]
        return l[0]
    
    elif len(unique) == 2:
        p, q = unique
        if l.count(p) == 3 or l.count(q) == 3:
            # 세 개 같고 하나 다름: [1,3]
            p, q = (p, q) if l.count(p) == 3 else (q, p)
            return (10 * p + q) ** 2
        else:
            # 두 쌍: [2,2]
            return (p + q) * abs(p - q)
    
    else:  # len(unique) == 3
        for n in unique:
            if l.count(n) == 2:
                q, r = [x for x in unique if x != n]
                return q * r