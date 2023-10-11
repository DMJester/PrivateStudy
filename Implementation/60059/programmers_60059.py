def rotate_key(key, m):
    case_list = [[[0] * m for _ in range(m)] for _ in range(4)]
    
    for angle in range(4):
        for y in range(m):
            for x in range(m):
                if angle == 0:
                    case_list[angle][y][x] = key[y][x]
                elif angle == 1:
                    case_list[angle][x][m-1-y] = key[y][x]
                elif angle == 2:
                    case_list[angle][m-1-y][m-1-x] = key[y][x]
                elif angle == 3:
                    case_list[angle][m-1-x][y] = key[y][x]
    return case_list

def make_match(lock, n, m, match_size):
    match = [[0] * match_size for _ in range(match_size)]
    
    for y in range(n):
        for x in range(n):
            match[y+m-1][x+m-1] = lock[y][x]
    
    return match

def check_match(match, n, m):
    sum_v = 0
    for y in range(m-1, (m-1) + n):
        for x in range(m-1, (m-1) + n): 
            if match[y][x] == 1:
                sum_v += 1
    
    if sum_v == (n*n):
        return True      
    else:
        return False

def solution(key, lock):
    res = False
    
    m = len(key)
    n = len(lock)
    
    key_case = rotate_key(key, m)
    
    match_size = ((m - 1) * 2) + n
    match = make_match(lock, n, m, match_size)
    my = 0;
    mx = 0;
    stop = False
    
    if check_match(match, n, m):
        res = True
        return res
    
    for angle in range(4):
        stop = False
        for y in range(match_size - (m-1) ):
            for x in range(match_size - (m-1) ):
                for my in range(m):
                    for mx in range(m):
                        match[y+my][x+mx] += key_case[angle][my][mx]
                
                if check_match(match, n, m):
                    res = True
                    return res
                else :
                    match = make_match(lock, n, m, match_size)
    
    return res