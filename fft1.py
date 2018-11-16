# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def main():
    # データのパラメータ
    N = 16             # サンプル数
    dt = 0.1          # サンプリング間隔
    fq1, fq2 = 2, 4    # 周波数
    t = np.arange(0, N*dt, dt) # 時間軸

    # 時間信号を生成（周波数10の正弦波+周波数20の正弦波+ランダムノイズ）
    f = np.sin(2*np.pi*fq1*t) + np.sin(2*np.pi*fq2*t) + 0.3 * np.random.randn(N)

    # 時間信号をCSVファイルに出力（小数点第二位まで）
    np.savetxt("data.csv", f, fmt='%.3f')


if __name__ == "__main__":
    main()

