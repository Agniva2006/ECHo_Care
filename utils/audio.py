import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf


FS = 16000


def record_audio(duration=6, filename="input.wav"):
    rec = sd.rec(int(duration * FS), samplerate=FS, channels=1, dtype='int16')
    sd.wait()
    write(filename, FS, rec)
    return filename


def play_audio(path):
    data, fs = sf.read(path)
    sd.play(data, fs)
    sd.wait()