# Question: Pizza Payments
# Categories: 7 Kyu

def michael_pays(cost: int) -> int:
    if cost < 5:
        return round(cost, 2)

    kate_contribution = (33.33 / 100) * cost
    
    if kate_contribution > 10:
        kate_contribution = 10

    michael_contribution = cost - kate_contribution
    return round(michael_contribution, 2)