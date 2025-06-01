# Question: Area or Perimeter
# Categories: 8 Kyu

def area_or_perimeter(length: int , width: int) -> int:
    if length == width:
        return length * width

    return 2 * (width + length)