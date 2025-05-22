# Question: The Solar System - Jumbled Planets
# Categories: 7 Kyu

def jumbled_solar_system(solar_system: list[str]) -> list[str]:
    '''
        Asteroid < Pluto < Mercury < Mars < Venus < Earth < Neptune < Uranus < Saturn < Jupiter
    '''
    celestial_body_size_in_asc_order = ['Asteroid', 'Pluto', 'Mercury', 'Mars', 'Venus', 'Earth', 'Neptune', 'Uranus', 'Saturn', 'Jupiter']
    result = []
    
    for i in range(1, len(solar_system)):
        previous_celestial_body = solar_system[i - 1]
        current_celestial_body = solar_system[i]
        
        if previous_celestial_body in celestial_body_size_in_asc_order[:celestial_body_size_in_asc_order.index(current_celestial_body)]:
            result.append('>')
        
        elif previous_celestial_body in celestial_body_size_in_asc_order[celestial_body_size_in_asc_order.index(current_celestial_body) + 1:]:
            result.append('<')
        
        else:
            result.append('=')
    
    return result