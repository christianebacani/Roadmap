# Question: Free pizza
# Categories: 6 Kyu

def pizza_rewards(customers: dict[str, list[int]], min_orders: int, min_price: int) -> set:
    result = []

    for name, orders in customers.items():
        total_qualified_orders = 0

        for order in orders:
            if order >= min_price:
                total_qualified_orders += 1
        
        if total_qualified_orders >= min_orders:
            result.append(name)
    
    return set(result)