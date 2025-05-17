# Question: Beginner Series #2 Clock
# Categories: 8 Kyu

def past(h: int, m: int, s: int) -> int:
    milliseconds = 0

    if h > 0:
        milliseconds += (h * 3600000)
    
    if m > 0:
        milliseconds += (m * 60000)
    
    if s > 0:
        milliseconds += (s * 1000)
    
    return milliseconds