# Question: Determine offspring sex based on genes XX and XY chromosomes
# Categories: 8 Kyu

def chromosome_check(chromosome: str) -> str:
    if 'Y' in chromosome:
        return 'Congratulations! You\'re going to have a son.'
    
    return 'Congratulations! You\'re going to have a daughter.'