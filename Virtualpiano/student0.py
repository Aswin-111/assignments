import numpy as np
import simpleaudio as sa
#generate a Numpy array of a wave

samplerate = 44100
#this function returns a dictionary
def piano_notes():
    #we are only creating
    #white keys are in Uppercase and black keys are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
#We can use vase_freq(c4) to calculate all the upcoming octaves and frequencies of the whole octave
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0
    return note_freqs
# Function takes the "frequecy" and "time_duration" for a wave as the parameter and returns a "numpy array" of values  
def wave(freq, duration=0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
#Implementation of mathematical equation for generating the wave
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave
#this function makes loops    
def song(music_notes):
    notefreqs = piano_notes()
    #This code loops through all music_notes given as string and remove the "-" symvol and find all the frequncies of the notes given
    song = [wave(notefreqs[note]) for note in music_notes.split('-')]
    #the notes are then concatanated using np.concatanate function
    song = np.concatenate(song)
    return song.astype(np.int16)
    

#the notes of the song
music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C'
#song function call and passes musicnotes as argument
data = song(music_notes)

# start playing the notes
play_obj = sa.play_buffer(data.astype(np.int16), 1,2, samplerate)

# continue playvack

play_obj.wait_done()
