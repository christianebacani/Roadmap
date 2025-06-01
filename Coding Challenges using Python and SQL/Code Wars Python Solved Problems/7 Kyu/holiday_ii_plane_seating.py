# Question: Holiday II - Plane Seating
# Categories: 7 Kyu

def plane_seat(user_plane_section_sector: str) -> str:
    plane_sections = {
        'Front': [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
        ],
        'Middle': [
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
        ],
        'Back': [
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60
        ]
    }
    plane_sectors = {
        'Left': 'ABC',
        'Middle': 'DEF',
        'Right': 'GHK'
    }
    
    user_plane_section, user_plane_sector = '', ''
    
    for i in range(len(user_plane_section_sector)):
        if user_plane_section_sector[i].isdigit():
            user_plane_section += user_plane_section_sector[i]
        
        else:
            user_plane_sector += user_plane_section_sector[i]
    
    if int(user_plane_section) < 1 or int(user_plane_section) > 60:
        return 'No Seat!!'
    
    result = []

    for position, plane_section in plane_sections.items():
        if int(user_plane_section) in plane_section:
            result.append(position)
    
    for position, plane_sector in plane_sectors.items():
        if user_plane_sector in plane_sector:
            result.append(position)
    
    if len(result) != 2:
        return 'No Seat!!'

    return '-'.join(result)