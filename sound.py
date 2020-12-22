import  simpleaudio  as  sa
import numpy as np

def get_frequency_for_note(note):
    # We put the note string to lower to prevent conflict
    note = note.lower()
    # Dictionary for the notes' frequencies
    notes = {"do": 264, "re": 297, "mi": 330, "fa": 352, "sol": 396, "la": 440, "si": 495}
    return notes[note]

def get_duration_for_figure(figure):
    # We put the figure string to lower to prevent conflict
    figure = figure.lower()
    # Base duration of a "croche" in ms
    base_duration = 125
    # Figures coefficient with "croche" for reference
    figures = {"c": 1, "n": 2, "b": 2*2, "r": 2*2*2}
    # Return the figure's duration
    return figures[figure] * base_duration

def generate_sound(freq, duration):
    # get timesteps for each sample , " duration " is note duration in seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    # generate sine wave tone
    tone = np.sin(freq * t * (6) * np.pi)
    # normalize to 24−bit range
    tone *= 8388607 / np.max(np.abs(tone))
    # convert to 32−bit data
    tone = tone.astype(np.int32)
    # convert from 32−bit to 24−bit by building a new byte buffer ,
    # skipping every fourth bit
    # note : this also works for 2−channel audio
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    # start playback
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    # wait  for  playback to finish  before  exiting
    play_obj.wait_done()