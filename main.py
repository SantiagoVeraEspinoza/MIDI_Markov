import midi
import con_rand as rand
import sample

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

sample.take_samples('base_weights.txt', 'final_weights.txt')

with open('final_weights.txt', 'r') as file:
    lines = file.readlines()

    for i, source_note in enumerate(adj_list):
        weights = lines[i].strip().split()
        for j, target_note in enumerate(adj_list[source_note]):
            adj_list[source_note][target_note] = float(weights[j])

    file.close()

def get_initial_note():
    notes = list(adj_list.keys())
    step = 1 / len(notes)
    rand_num = rand.rand_normal()

    acum = step
    n = 0
    
    while acum < rand_num:
        acum += step
        n += 1

    return notes[n]

def get_next_note(curr_note):
    notes = list(adj_list.keys())
    tran = [adj_list[curr_note][target_note] for target_note in adj_list[curr_note]]
    rand_num = rand.rand_normal()

    acum = tran[0]
    n = 0

    while acum < rand_num:
        n += 1
        acum += tran[n]

    return notes[n]

CURR_NOTE = get_initial_note()
MELODY = [CURR_NOTE]
MELODY_LENGHT = 30

for n in range(MELODY_LENGHT):
    MELODY.append(get_next_note(CURR_NOTE))

for note in MELODY:
    print(note, end=' ')
print()

midi.generate(MELODY)
