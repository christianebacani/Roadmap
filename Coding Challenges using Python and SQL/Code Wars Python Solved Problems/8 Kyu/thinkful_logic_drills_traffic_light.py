# Question: Thinkful - Logic Drills: Traffic light
# Categories: 8 Kyu

def update_light(current: str) -> str:
    traffic_light_changes = {
        'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
    }

    return traffic_light_changes[current]