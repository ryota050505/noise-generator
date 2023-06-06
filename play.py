import sounddevice as sd
import soundfile as sf

filepath = "./test.wav"
sig, sr = sf.read(filepath, always_2d=True)
sd.play(sig, sr)

sd.wait()
print("End")
