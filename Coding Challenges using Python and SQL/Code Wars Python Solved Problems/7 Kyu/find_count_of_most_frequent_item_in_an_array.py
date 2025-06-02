# Question: Find Count of Most Frequent Item in an Array
# Categoreies: 7 Kyu

def most_frequent_item_count(collection: list[int]) -> int:
    frequencies = []

    for i in range(len(collection)):
        frequencies.append(collection.count(collection[i]))
    
    return max(frequencies, default=0)