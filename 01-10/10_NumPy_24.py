import numpy as np


def peak_indexes(x):
 # x เป็นอาเรย์เก็บจ านวนต่าง ๆ
 # คืนอาเรย์ที่เก็บต าแหน่งใน x ที่เป็น "ยอด"
    left = np.concatenate(([np.Infinity], x[:-1]), axis=0)
    right = np.concatenate((x[1:], [np.Infinity]), axis=0)
    return np.where((x > left) & (x > right))[0]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())
