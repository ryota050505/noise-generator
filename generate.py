import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

def white_noise(fs, length):
  # 一様乱数
  return np.random.random(size=length) * 2 - 1

def pink_noise(fs, length):
  tmp = white_noise(fs, length)
  # 周波数領域の値に変換
  S = np.fft.rfft(tmp)
  # 低周波ほどfilterが小さい
  fil = 1 / (np.arange(len(S)) + 1)
  # 高周波になるほど値が小さくなる
  S = S * fil
  # 逆FFTにより音声に戻す
  s = np.fft.irfft(S)
  # 音声のピークの箇所を割って
  s /= np.max(np.abs(s))
  return s

fs = 48000
length = 2 ** 18
s = pink_noise(fs, length)
write("./test.wav", rate=fs, data=s)
