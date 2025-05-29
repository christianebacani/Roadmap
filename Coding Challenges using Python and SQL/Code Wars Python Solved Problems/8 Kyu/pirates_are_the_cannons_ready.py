# Question: Pirates!! Are the Cannons ready!??
# Categories: 8 Kyu

def cannons_ready(gunners: dict[str, str]) -> str:
    for _, is_ready in gunners.items():
        if is_ready == 'nay':
            return 'Shiver me timbers!'
    
    return 'Fire!'