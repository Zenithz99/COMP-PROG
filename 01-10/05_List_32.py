n = int(input()) # อ่านจ านวนค าสั่ง
queue_number = 0
in_queue = []
call = []
total_order = 0
total_time = 0
for k in range(n):
    c = input().split() # อ่านข้อมูลค าสั่ง
    if c[0] == 'reset':
        queue_number = int(c[1])
    elif c[0] == 'new':
        in_queue.append([queue_number,int(c[1])])
        print("ticket",queue_number)
        queue_number += 1
    elif c[0] == 'next':
        call = in_queue[0]
        in_queue.pop(0)
        print("call",call[0])
    elif c[0] == 'order':
        df = int(c[1]) - call[1]
        print("qtime {} {}".format(call[0],df))
        total_time += df
        total_order += 1
    elif c[0] == 'avg_qtime':
        print("avg_qtime",round(total_time/total_order,4))
