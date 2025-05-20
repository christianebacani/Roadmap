# Question: Filter out the geese
# Categories: 8 Kyu

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds: list[str]) -> list[str]:
    birds = [bird for bird in birds if bird not in geese]

    return birds