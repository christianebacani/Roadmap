# Question: Most sales
# Categories: 7 Kyu

def top3(products: list[str], amounts: list[int], prices: list[int]) -> list[str]:
    product_and_revenue = {}

    for i in range(len(products)):
        revenue = amounts[i] * prices[i]
        product_and_revenue[products[i]] = revenue
    
    sorted_distinct_revenue = sorted(list(set(product_and_revenue.values())), reverse=True)
    result = []

    for i in range(len(sorted_distinct_revenue)):
        for product, revenue in product_and_revenue.items():
            if sorted_distinct_revenue[i] == revenue:
                result.append(product)
    
    return result[:3]