# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import ast


def main():
    # データのパラメータ
    N = 16  # サンプル数
    dt = 0.1  # サンプリング間隔

    # CSVのロード(データ型は虚数：complex)
    F = np.genfromtxt("fdata.csv", dtype='complex', converters={0: lambda s: ast.literal_eval(s.decode())})

    # 高速逆フーリエ変換
    f = np.fft.ifft(F)

    # 実部の値のみ取り出し
    f = f.real

    # 変換後のデータ（時間領域）を保存
    np.savetxt("data2.csv", f, fmt='%.3f')

    x= np.arange(0,N*dt,dt)
    plt.plot(x,f)
    plt.show()


if __name__ == "__main__":
    main()