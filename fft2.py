# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def main():
    f = np.genfromtxt("data.csv", dtype='float')

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 変換後のデータ（周波数領域）を保存
    np.savetxt("fdata.csv", F, fmt='%.3f')

    N = 16             # サンプル数
    dt = 0.1          # サンプリング間隔

    print(1/dt/2,1/dt/N)

    x= np.arange(0,1/dt/2,1/dt/N/2)

    print (x)
    plt.plot(x,F.real)
    plt.show()


if __name__ == "__main__":
    main()