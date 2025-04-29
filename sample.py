import mido
import math
import os
import con_rand as rand
import random

NOTES = {
    'do3': 48,  'do#3': 49, 're3': 50,  're#3': 51, 'mi3': 52,
    'fa3': 53,  'fa#3': 54, 'sol3': 55, 'sol#3': 56, 'la3': 57, 'la#3': 58, 'si3': 59,
    'do4': 60,  'do#4': 61, 're4': 62,  're#4': 63, 'mi4': 64,
    'fa4': 65,  'fa#4': 66, 'sol4': 67, 'sol#4': 68, 'la4': 69, 'la#4': 70, 'si4': 71,
    'do5': 72
}

adj_list = {
    'DO3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'DO#3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'RE3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'RE#3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'MI3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'FA3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'FA#3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SOL3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SOL#3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'LA3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'LA#3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SI3': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'DO4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'DO#4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'RE4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'RE#4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'MI4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'FA4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'FA#4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SOL4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SOL#4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'LA4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'LA#4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}, 
    'SI4': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0},
    'DO5': {'DO3': 0, 'DO#3': 0, 'RE3': 0, 'RE#3': 0, 'MI3': 0, 'FA3': 0, 'FA#3': 0, 'SOL3': 0, 'SOL#3': 0, 'LA3': 0, 'LA#3': 0, 'SI3': 0, 'DO4': 0, 'DO#4': 0, 'RE4': 0, 'RE#4': 0, 'MI4': 0, 'FA4': 0, 'FA#4': 0, 'SOL4': 0, 'SOL#4': 0, 'LA4': 0, 'LA#4': 0, 'SI4': 0, 'DO5': 0}
}

def get_midi_notes(path):
    # Carga el archivo MIDI
    mid = mido.MidiFile(path)

    # Lista para guardar las notas
    notes = []

    # Recorremos todos los mensajes en todas las pistas
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:
                notes.append(msg.note)

    return notes

def convert_to_notes(note_list):
    n_note_list = []
    for note in note_list:
        n_note_str = random.choice(list(adj_list.keys()))
        for note_str, note_num in NOTES.items():
            if note == note_num:
                n_note_str = note_str

        n_note_list.append(n_note_str)

    return n_note_list

def preload_transition_matrix(path):
    with open(path, 'r') as file:
        lines = file.readlines()

        for i, source_note in enumerate(adj_list):
            weights = lines[i].strip().split()
            for j, target_note in enumerate(adj_list[source_note]):
                adj_list[source_note][target_note] = float(weights[j])

        file.close()

def save_transition_matrix(path):
    with open(path, 'w') as file:
        for source_note in adj_list:
            line = ''
            for target_note in adj_list[source_note]:
                adj_list[source_note][target_note] = math.trunc(adj_list[source_note][target_note] * 10000) / 10000
                line += f"{adj_list[source_note][target_note]} "
            line += "\n"

            file.write(line)
        file.close()

def summarize_transition_matrix(sample_file):
    notes = convert_to_notes(get_midi_notes(sample_file))

    for i in range(len(notes) - 1):
        source_note = notes[i]
        target_note = notes[i + 1]

        adj_list[source_note.upper()][target_note.upper()] += 1

    return adj_list

def laplace_smoothing(k=4):
    for source_note in adj_list:
        for target_note in adj_list[source_note]:
            adj_list[source_note][target_note] += k

    return adj_list

def normalize():
    for source_note in adj_list:
        total_sum = sum([num for num in adj_list[source_note].values()])

        for target_note in adj_list[source_note]:
            adj_list[source_note][target_note] = adj_list[source_note][target_note] / total_sum

    return adj_list

def take_samples(source, target):
    preload_transition_matrix(source)

    base_dir = './samples'
    for file in os.listdir(base_dir):
        sample_path = os.path.join(base_dir, file)
        summarize_transition_matrix(sample_path)

    laplace_smoothing(k=4)
    normalize()

    save_transition_matrix(target)