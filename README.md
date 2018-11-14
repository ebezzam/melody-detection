# Fun Fourier Transform Workshop: Whistle Detector

Check out this [Colaboratory notebook](https://colab.research.google.com/drive/1wEKM7zLxhBYGloXkbbagNMRmYyjXWHzN) for the exercises!
- Press "Open in Playground" under the toolbar in order to make edits.
- You will have to be signed into your Google Account to run the notebook.

If you are having technical difficulties or prefer running locally, no problem!
Go to `"File > Download .ipynb"`. Locally, you don't need to run the cells with following 
lines of code:
```python
from google.colab import files
files.upload()
```
Just make sure that the WAV files are in the same directory as the notebook.

Accompanying slides can be found [here](https://docs.google.com/presentation/d/1ffcKawVvajIQkwZren9lByPTOZ6NsWaINB1XzMTDVgk/edit?usp=sharing)!

You can request for the solutions [here](https://colab.research.google.com/drive/1wEtgSBNuE_JKU_9OKmZIha-8HztgWdlL#scrollTo=GWbrFvTp70_f)
or by emailing me: ebezzam[at]gmail[dot]com

## Requirements if running locally

Make sure you have the packages specified in `requirements.txt`:
`matplotlib` and `pyserial` are only needed for the NeoPixels demo.

## Live testing of the whistle detector

Once you have completed the following functions from the notebook:
```python
transcribe
estimateBaseFreq
dtw
```

Copy them to the `utils.py` file.

You can then run `demo_audio_feedback.py` to test the Whistle Detector!
A command line prompt will appear; you can press `"r+Enter"` to record
yourself and see if you can match the "passphrase".
You should hear a bell if you whistled the correct tune and a buzzer if not.

If you have an Arduino and a [NeoPixels 60 LED Ring](https://www.adafruit.com/product/2874), 
you can run `demo_neopixels.py` for a whistle detector that provides visual
feedback (green for correct, red for incorrect). You will first have to flash
your Arduino with `neopixels_firmware/neopixels_firmware.ino`.

## Tuning the whistle detector

Think you got it right but it's not detecting the melody? Or perhaps your 
detection thinks everything is correct (false positives). 

You can tune the whistle detector by adjusting the following parameters:
- `THRESHOLD` at the top of the `demo_*.py` scripts. A lower value will be
more selective, while a higher value will yield a less strict detector.
- `PEAK_WIDTH` and `E_RATIO` in the `utils.transcribe` function.

Otherwise, you can tune your own whistling ;)

## References

Workshop content is modified from material by [Paolo Prandoni](https://github.com/prandoni).

WAV file sources:
- In workshop: from Paolo Prandoni
- Bell sound: https://freesound.org/people/InspectorJ/sounds/411089/
- Buzzer sound: https://freesound.org/people/hypocore/sounds/164089/