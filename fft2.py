# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def main():
    f = np.genfromtxt("data.csv", dtype='float')

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 変換後のデータ（周波数領域）を保存
    np.savetxt("fdata.csv", F, fmt='%.3f')

if __name__ == "__main__":
    main()