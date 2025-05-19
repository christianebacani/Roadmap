# Question: The Office IV - Find a Meeting Room
# Categories: 7 Kyu

def meeting(rooms: list[str]) -> int:
    try:
        return rooms.index('O')
    
    except:
        return 'None available!'