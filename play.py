import sounddevice as sd
import soundfile as sf
import sys

filepath = sys.argv[1]
sig, sr = sf.read(filepath, always_2d=True)
sd.play(sig, sr)

sd.wait()
print("End")
