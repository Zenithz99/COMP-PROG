def spiral_square(n): # n is a positive odd number
    mid = n // 2
    cur = [mid , mid]
    num = 1
    dir_list = [[0,1] , [-1,0] , [0,-1] , [1,0]]
    cur_dir = 0
    round = 1
    square = [[0 for i in range(n)] for i in range(n)]
    square[cur[0]][cur[1]] = num
    while (num <= n*n) :
        for i in range(round) :
            num += 1
            if num > n*n : break
            cur[0] += dir_list[cur_dir][0]
            cur[1] += dir_list[cur_dir][1]
            square[cur[0]][cur[1]] = num
        

        if (cur_dir == 1 or cur_dir == 3) : round += 1
        cur_dir = (cur_dir+1) % 4
    return square 


def print_square(S):
    # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())