# Question: Thinkful - Number Drills: Blue and red marble
# Categories: 8 Kyu

def guess_blue(blue_start: int, red_start: int, blue_pulled: int, red_pulled: int) -> float:
    available_blue_marbles = blue_start - blue_pulled
    available_red_marbles = red_start - red_pulled
    total_available_marbles = available_blue_marbles + available_red_marbles

    return available_blue_marbles / total_available_marbles