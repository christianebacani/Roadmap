# Question: Quarter of the year
# Categories: 8 Kyu

def quarter_of(month: int) -> int:
    quarter_and_month_range= {
        1: range(1, 4),
        2: range(4, 7),
        3: range(7, 10),
        4: range(10, 13)
    }

    for quarter, range_month in quarter_and_month_range.items():
        if month in range_month:
            return quarter