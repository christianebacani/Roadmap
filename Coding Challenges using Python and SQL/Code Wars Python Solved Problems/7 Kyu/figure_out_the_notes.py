# Question: Figure Out the Notes
# Categories: 7 Kyu

def what_note(note: str, fret: int) -> str:
    list_of_notes = [
        'A',
        'A#',
        'B',
        'C',
        'C#',
        'D',
        'D#',
        'E',
        'F',
        'F#',
        'G',
        'G#'
    ]

    for i in range(len(list_of_notes)):
        if list_of_notes[i] == note.upper():
            try:
                return list_of_notes[i + fret]

            except:
                return list_of_notes[(i + fret) % len(list_of_notes)]