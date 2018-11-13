import neopixels
from utils import transcribe, estimateBaseFreq, dtw
import sounddevice as sd
from scipy.io import wavfile
import time

led_ring_address = '/dev/cu.usbmodem1421'
led_ring = neopixels.NeoPixels(usb_port=led_ring_address)

def test_led_ring(led_ring):
    led_ring.lightify_mono(rgb=[0, 150, 0])
    time.sleep(2)

    led_ring.lightify_mono(rgb=[150, 0, 0])
    time.sleep(2)

    led_ring.lightify_mono(rgb=[0, 0, 0])


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
    result_light(d, thresh)


def result_light(score, thresh):

    if score < thresh:
        print("OPEN SESAME! Score: {}".format(score))
        led_ring.lightify_mono(rgb=[0, 150, 0])
        time.sleep(1)
    else:
        print("WRONG! Score: {}".format(score))
        led_ring.lightify_mono(rgb=[150, 0, 0])
        time.sleep(1)


if __name__ == "__main__":

    # provide passphrase here
    Fs, ppA = wavfile.read("wav_files/ppA.wav")

    while True:
        print('#' * 80)
        print("Press 'r + Enter' to record and 'q + Enter' to quit")
        char = input()
        if char == 'r':
            keylock(3, Fs, ppA)
        elif char == 'q':
            break
