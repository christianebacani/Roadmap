# Question: White or Black?
# Categories: 7 Kyu

def square_color(tile_name: str, tile_number: int) -> str:
    tile_name_and_tiles = {
        'a': [0, 1, 0, 1, 0, 1, 0, 1],
        'b': [1, 0, 1, 0, 1 , 0, 1, 0],
        'c': [0, 1, 0, 1, 0, 1, 0, 1],
        'd': [1, 0, 1, 0, 1 , 0, 1, 0],
        'e': [0, 1, 0, 1, 0, 1, 0, 1],
        'f': [1, 0, 1, 0, 1 , 0, 1, 0],
        'g': [0, 1, 0, 1, 0, 1, 0, 1],
        'h': [1, 0, 1, 0, 1 , 0, 1, 0]
    }

    for key, value in tile_name_and_tiles.items():
        if tile_name != key:
            continue

        for index, tiles in enumerate(value):
            index += 1

            if tile_number != index:
                continue

            if tiles == 1:
                return 'white'
            
            else:
                return 'black'