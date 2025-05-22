# Question: The Solar System - Planet Mnemonic
# Categories: 7 Kyu

def is_planet_mnemonic_correct(solar_system: list[str], mnemonic: str) -> bool:
    if solar_system == [] and mnemonic == '':
        return True

    mnemonic = [planet[0] for planet in mnemonic.split()]
    solar_system = [planet[0] for planet in solar_system if planet != 'Asteroid']

    if mnemonic == solar_system:
        return True
    
    return False