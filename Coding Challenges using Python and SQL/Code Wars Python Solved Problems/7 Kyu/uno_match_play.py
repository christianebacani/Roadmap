# Question: Uno Match Play
# Categories: 7 Kyu

def can_play(hand: list[str], face_up: str) -> bool:
    face_up_color = face_up.split()[0]
    face_up_number = face_up.split()[1]
    
    for i in range(len(hand)):
        hand_color = hand[i].split()[0]
        hand_number = hand[i].split()[1]

        if (hand_color in face_up_color) or (hand_number in face_up_number):
            return True
    
    return False