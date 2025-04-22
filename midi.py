from mido import Message, MidiFile, MidiTrack

NOTES = {
    'do3': 48,  'do#3': 49, 're3': 50,  're#3': 51, 'mi3': 52,
    'fa3': 53,  'fa#3': 54, 'sol3': 55, 'sol#3': 56, 'la3': 57, 'la#3': 58, 'si3': 59,
    'do4': 60,  'do#4': 61, 're4': 62,  're#4': 63, 'mi4': 64,
    'fa4': 65,  'fa#4': 66, 'sol4': 67, 'sol#4': 68, 'la4': 69, 'la#4': 70, 'si4': 71,
    'do5': 72
}

DEFAULT_DURATION = 350

def generate(notes):
    # Create a new MIDI file and a track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Add a program change (select instrument), 0 is usually piano
    track.append(Message('program_change', program=0, time=0))

    melody = []

    # Define a simple melody: (note, duration)
    for note in notes:
        note = str.lower(note)

        melody.append((NOTES[note], DEFAULT_DURATION))
        
    # Add note on and note off messages
    for note, duration in melody:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=duration))

    # Save the MIDI file
    mid.save('melody.mid')