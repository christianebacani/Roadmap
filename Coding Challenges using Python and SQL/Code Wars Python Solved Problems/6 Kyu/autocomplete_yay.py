# Question: Autocomplete! Yay!
# Categories: 6 Kyu

def autocomplete(prefix: str, arr: list[str]) -> list[str]:
    formatted_prefix = ''

    for i in range(len(prefix)):
        if prefix[i].isalpha():
            formatted_prefix += prefix[i]
    
    prefix = formatted_prefix
    result = []

    for i in range(len(arr)):
        if arr[i].startswith(prefix.lower()) or arr[i].startswith(prefix.upper()) or arr[i].startswith(prefix.capitalize()):
            result.append(arr[i])
    
    return result[:5]