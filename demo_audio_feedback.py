from utils import transcribe, estimateBaseFreq, dtw
import sounddevice as sd
from scipy.io import wavfile
import sys


WHISTLE_PASSPHRASE = "wav_files/ppA.wav"  # you can also record your own! Record at 16 kHz
DURATION = 3                              # length that you will record for input whistles
THRESHOLD = 3                             # threshold after DTW comparison


def keylock(dur, Fs, original_key, thresh=3):
    """

    :param dur: duration of recording in seconds
    :param Fs: sampling rate
    :param original_key:
    :param thresh: threshold for DTW comparison
    :return:
    """

    print("STARTING RECORDING")
    in_key = sd.rec(int(dur * Fs), samplerate=Fs, channels=1, blocking=True).flatten()
    print("FINISHED RECORDING")

    k = []
    for audio in (in_key, original_key):
        t = transcribe(Fs, audio)
        k.append(t / estimateBaseFreq(t))
    d = dtw(k[0], k[1])

    # put your desired action here!
    result_audio(d, thresh)


def result_audio(score, thresh):

    if score < thresh:
        print("OPEN SESAME! Score: {}".format(score))
        Fs, bell = wavfile.read("wav_files/bell_short.wav")
        sd.play(bell, samplerate=Fs, blocking=True)
    else:
        print("WRONG! Score: {}".format(score))
        Fs, buzzer = wavfile.read("wav_files/buzzer_short.wav")
        sd.play(buzzer, samplerate=Fs, blocking=True)


if __name__ == "__main__":

    python_version = 2
    if sys.version_info > (3, 0):
        python_version = 3

    # provide passphrase here
    Fs, ppA = wavfile.read(WHISTLE_PASSPHRASE)

    while True:
        print('#' * 80)
        print("Press 'r + Enter' to record and 'q + Enter' to quit")
        if python_version == 2:
            char = raw_input()
        else:
            char = input()
        if char == 'r':
            keylock(DURATION, Fs, ppA, thresh=THRESHOLD)
        elif char == 'q':
            break
