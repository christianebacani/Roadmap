# Question: Swap the head and the tail
# Categories: 7 Kyu

def swap_head_tail(arr: list[int]) -> list[int]:
    if len(arr) % 2 != 0:
        middle_index = len(arr) // 2
        head = arr[:middle_index]
        tail = arr[middle_index + 1:]
        
        return tail + [arr[middle_index]] + head
    
    else:
        delimiter = len(arr) // 2
        head = arr[:delimiter]
        tail = arr[delimiter:]
        
        return tail + head