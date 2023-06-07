import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import sys

def white_noise(fs, length):
  # 一様乱数
  return np.random.random(size=length) * 2 - 1

# ローパス * ハイパス
def pink_noise(fs, length):
  tmp = white_noise(fs, length)
  # 周波数領域の値に変換
  S = np.fft.rfft(tmp)
  # 低周波ほどfilterが小さい
  # arr = np.arange(len(S)) + 1 # test1.wav
  # arr = np.concatenate([np.arange(len(S)/2) + 1, np.arange(len(S)/2 - 2, -1, -1) + 1]) # test2.wav
  arr = np.concatenate([np.linspace(0, len(S), int(len(S)/2)+1) + 1, np.full(int(len(S)/2), len(S)) + 1]) # test3.wav
  fil = 1 / arr
  # 高周波になるほど値が小さくなる
  S = S * fil
  # 逆FFTにより音声に戻す
  s = np.fft.irfft(S)
  # 一番大きい箇所の振幅で割る
  s /= np.max(np.abs(s))
  return s

file_name = sys.argv[1]
fs = 48000
length = 2 ** 18
s = pink_noise(fs, length)
write(file_name, rate=fs, data=s)
