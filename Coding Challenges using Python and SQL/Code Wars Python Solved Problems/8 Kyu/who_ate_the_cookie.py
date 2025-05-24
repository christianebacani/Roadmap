# Question: Who ate the cookie?
# Categories: 8 Kyu

def cookie(x: str | float | int | bool | None) -> str:
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'

    elif x is True or x is False or x is None:
        return 'Who ate the last cookie? It was the dog!'
    
    else:
        return 'Who ate the last cookie? It was Monica!'