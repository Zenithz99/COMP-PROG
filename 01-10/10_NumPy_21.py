import numpy as np


def sum_2_rows(M):
 # คืนผลที่ได ้จากการรวมจ านวนในคอลัมน์เดียวกันของแถวที่ติดกันทีละคู่แถว
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 4, 6, 8, 10],
 # [ 4, 5, 6, 7], [20, 22, 24, 26]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    m1 = M[::2, ::]
    m2 = M[1::2, ::]
    return m1 + m2


def sum_left_right(M):
 # คนืผลทไี่ ดจ้ากการรวมจ านวนของครงึ่ ซา้ยกับครงึ่ ขวาของ M
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 2, 4],
 # [ 4, 5, 6, 7], [10, 12],
 # [ 8, 9, 10, 11], [18, 20],
 # [12, 13, 14, 15]] [26, 28]]
    leng = M.shape[1]
    m1 = M[::, :leng//2]
    m2 = M[::, leng//2::]
    return m1 + m2


def sum_upper_lower(M):
 # คืนผลที่ได ้จากการรวมจ านวนของครึ่งบนกับครึ่งล่างของ M
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 8, 10, 12, 14],
 # [ 4, 5, 6, 7], [16, 18, 20, 22]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    leng = M.shape[0]
    m1 = M[:leng//2, ::]
    m2 = M[leng//2::, ::]
    return m1 + m2


def sum_4_quadrants(M):
 # คืนผลที่ได ้จากการแบ่ง M เป็น 4 จตุภาค และรวมจ านวนที่ต าแหน่งตรงกันในแต่ละจตุภาค
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[20, 24],
 # [ 4, 5, 6, 7], [36, 40]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    n = M.shape[0]
    m = M.shape[1]
    M1 = M[:n//2, :m//2]
    M2 = M[:n//2, m//2:]
    M3 = M[n//2:, m//2:]
    M4 = M[n//2:, :m//2]
    return M1+M2+M3+M4


def sum_4_cells(M):
 # คืนผลที่ได ้จากการรวมจ านวนที่ติดกัน 4 ตัว ตามรูปแบบในตัวอย่างข ้างล่างนี้
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[10, 18],
 # [ 4, 5, 6, 7], [42, 50]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    M1 = M[::2, ::2]
    M2 = M[::2, 1::2]
    M3 = M[1::2, ::2]
    M4 = M[1::2, 1::2]
    return M1 + M2 + M3 + M4


def count_leap_years(years):
 # years เป็นอาเรย์เก็บปี พ.ศ.
 # คืนจ านวนปีใน years ที่เป็นปีอทิกสุรทิน (ปีที่ ก.พ. มี 29 วัน)
    years -= 543
    return years[((years % 400) == 0) | (((years % 4) == 0) & ((years % 100) != 0))].shape[0]


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
