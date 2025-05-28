# Question: Crash Override
# Categories: 7 Kyu

def alias_gen(first_name: str, last_name: str) -> str:
    first_name_alias = {
        'A': 'Alpha',
        'B': 'Beta',
        'C': 'Cache',
        'D': 'Data',
        'E': 'Energy',
        'F': 'Function',
        'G': 'Glitch',
        'H': 'Half-life',
        'I': 'Ice',
        'J': 'Java',
        'K': 'Keystroke',
        'L': 'Logic',
        'M': 'Malware',
        'N': 'Nagware',
        'O': 'OS',
        'P': 'Phishing',
        'Q': 'Quantum',
        'R': 'RAD',
        'S': 'Strike',
        'T': 'Trojan',
        'U': 'Ultraviolet',
        'V': 'Vanilla',
        'W': 'WiFi',
        'X': 'Xerox',
        'Y': 'Y',
        'Z': 'Zero'
    }
    last_name_alias = {
        'A': 'Analogue',
        'B': 'Bomb',
        'C': 'Catalyst',
        'D': 'Discharge',
        'E': 'Electron',
        'F': 'Faraday',
        'G': 'Gig',
        'H': 'Hacker',
        'I': 'IP',
        'J': 'Jabber',
        'K': 'Killer',
        'L': 'Lazer',
        'M': 'Mike',
        'N': 'n00b',
        'O': 'Overclock',
        'P': 'Payload',
        'Q': 'Quark',
        'R': 'Roy',
        'S': 'Spy',
        'T': 'T-Rex',
        'U': 'Unit',
        'V': 'Virus',
        'W': 'Worm',
        'X': 'X',
        'Y': 'Yob',
        'Z': 'Zombie'
    }

    if not first_name[0].isalpha() or not last_name[0].isalpha():
        return 'Your name must start with a letter from A - Z.'
    
    return first_name_alias[first_name[0].upper()] + ' ' + last_name_alias[last_name[0].upper()]