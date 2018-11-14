import numpy as np


def transcribe(Fs, x, WHISTLE_MIN_HZ=700, WHISTLE_MAX_HZ=3000, WIN_LEN_MS=24):
    """
    WHISTLE_MIN_HZ (float) : minimum whistling frequency in Hz.
    WHISTLE_MAX_HZ (float) : maximum whistling frequency in Hz.
    WIN_LEN_MS (float) : assumed maximum whistle length in milliseconds. This will also be the STFT segment length.
    """

    # bins around the peak to detect peak energy
    PEAK_WIDTH = 3

    # energy ratio to detect whistled frames
    E_RATIO = 0.8

    # length of the segment in samples
    win_len = int(WIN_LEN_MS * Fs / 1000.0)

    # frequency resolution of the DFT
    freq_res = float(Fs) / win_len

    # THIS IS FOR YOU TO FIGURE OUT!
    try:
        # first and last frequency indices for the whistling range
        min_bin
        max_bin
    except:
        raise ValueError("Compute first and last frequency index for whistling range.")

    # normalize audio amplitude to 1
    x = np.array(x) / max(x)

    pitch = []
    for n in range(0, len(x) - win_len, win_len):

        segment = x[n:n + win_len]

        try:

            # THIS IS FOR YOU TO FIGURE OUT!
            # DFT square magnitude for the segment, extract over freq interval of interest. Hint: np.abs()
            segment_ft
            # location of the max
            peak

        except:
            raise ValueError("Compute DFT square magniture and peak.")

        # energy around the peak vs total energy
        k = np.sum(segment_ft[max(peak - PEAK_WIDTH, 0):min(peak + PEAK_WIDTH + 1, len(segment_ft))])

        # if whistled frame, append pitch (ignore all other segments)
        if k > E_RATIO * np.sum(segment_ft):
            pitch.append(freq_res * (peak + min_bin))

    return np.trim_zeros(np.array(pitch))


def estimateBaseFreq(s, THRESHOLD=2 ** (2 / 12)):
    """
    THRESHOLD (float) : to distinguish between notes, e.g. a whole tone (2**(2/12)).
    """

    # first note
    notes = []
    ix = 0
    for c in range(1, len(s)):

        # THIS IS FOR YOU TO FIGURE OUT!
        try:
            # add a new note only if we're jumping up or down at least a whole tone
            if CONDITION:
                notes.append(np.mean(s[ix:c]))
                ix = c
        except:
            raise ValueError("Fill in the condition for collecting notes for base frequency estimation.")

    return np.mean(np.array(notes))


def dtw(a, b):
    D = np.zeros((len(a), len(b)))
    D[1:, 0] = np.inf
    D[0, 1:] = np.inf
    for i in range(len(a)):
        for j in range(len(b)):
            # THIS IS FOR YOU TO FIGURE OUT!
            try:
                # contribution from a[i] and b[j]
                d
                # minimum distance to D[i,j]
                D[i, j]
            except:
                raise ValueError("Compute the minimum distance.")
    return D[-1, -1]

