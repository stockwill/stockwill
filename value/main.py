#!/usr/bin/env python3.7

import numpy as np


def get_val(distri, list_quater_eps, rewards):
    print(distri)
    d = list(map(lambda a: a[0]/a[1], distri))
    print(d)
    average = np.average(d)
    print("average distribution rate: ", average)

    eps = np.sum(list_quater_eps)
    eps = eps/len(list_quater_eps)*4
    print("expected eps: ", eps)

    std = np.std(list_quater_eps)
    print("std: ", std, " from list eps: ", list_quater_eps)
    mean = np.mean(list_quater_eps)
    print("mean: ", mean)
    # https://www.calculator.net/standard-deviation-calculator.html?numberinputs=0.99%2C+1.46%2C+0.3%2C+3.39&ctype=p&x=45&y=32
    # http://csie.nqu.edu.tw/smallko/ns2_old/confidence_interval.htm
    sem = std/np.sqrt(len(list_quater_eps))
    # print("sem: ", sem)

    for r in rewards:
        print("reward ", r, " ", (eps * average / r))

    for r in rewards:
        for change in [[68.3, 1], [90, 1.645], [95, 1.96], [99, 2.57]]:
            low = ((eps - sem * change[1]) * average / r)
            high = ((eps + sem * change[1]) * average / r)
            print("reward ", r, "[", low, ", ", high, "]", " for confidential interval: ", change[0])


def main():
    # get_val([[1.5,3.95], [2.5,4.47], [2,3.79], [2,4.58]], [1.4, 1.05, -0.23, 1.47], [0.05, 0.04]) # 2882
    # get_val([[6.2,8.36], [7,9.33], [5.6,7.5], [3.5,4.72]], [0.99, 1.46, 0.3, 3.39], [0.05, 0.04]) # 1326
    # get_val([[6.2,8.36], [7,9.33], [5.6,7.5], [3.5,4.72]], [0.99, 1.46], [0.05, 0.04]) # 1326
    # get_val([[0.44/2+0.54, 1.09], [0.53+0.43/2, 1.1], [0.72/2 + 0.48, 1.09], [3.5, 4.72]], [0.32, 0.37, 0.12, 0.29], [0.05, 0.04])# 2887
    #get_val([[1.7, 2.07], [1.5, 1.89], [1.42, 1.65], [1.5, 2.35]], [0.57, 0.56, 0.38, 0.55], [0.05, 0.04])# 2886
    #get_val([[1.5, 3.95], [2.5, 4.47], [2, 3.79], [2, 4.58]], [1.4, 1.05], [0.05, 0.04])# 2882
    #get_val([[10, 12.03], [9.5, 11.04], [9, 11.31], [7.5, 9.42]], [3.15, 3.14, 2.42, 3.51], [0.05, 0.04])# 1537
    # get_val([[3.75, 2.88], [3.75, 3.33], [3.75, 3.5], [3.75, 3.52]], [0.67, 0.68, 0.5, 0.8], [0.05, 0.04])# 4904
    # get_val([[5.6, 5.01], [5.6, 5.21], [5.6, 5.63], [5.6, 5.76]], [1.16, 1.13, 1.13, 1.21], [0.05, 0.04])# 3045
    #get_val([[4.8, 5.01], [4.94, 5.16], [5.49, 5.52]], [1.1, 1.08, 1.09, 1.1], [0.05, 0.04])# 2412
    #get_val([[0.61+0.61/2, 1.4], [0.49+0.74/2, 1.4], [0.43+1/2, 1.48], [0.43+0.87/2, 1.43]], [0.44, 0.29, 0.38, 0.36, 0.4], [0.05, 0.04])# 2884
    stock_multiplier = 1
    get_val([[0.61+0.61 * stock_multiplier, 1.4], [0.49+0.74 * stock_multiplier, 1.4],
             [0.43+1 * stock_multiplier, 1.48], [0.43+0.87 * stock_multiplier, 1.43]],
            [0.29, 0.38, 0.36, 0.4], [0.05, 0.04])# 2884



if __name__ == "__main__":
    main()

