# Question: Data Reverse
# Categories: 6 Kyu

def data_reverse(data: list[int]) -> list[int]:
    list_of_bytes = []
    
    for i in range(0, len(data), 8):
        byte = data[i : i + 8]
        list_of_bytes.append(byte)
    
    # Reverse the bytes
    list_of_bytes = list_of_bytes[::-1]
    result = []

    for i in range(len(list_of_bytes)):
        for j in range(len(list_of_bytes[i])):
            result.append(list_of_bytes[i][j])
    
    return result