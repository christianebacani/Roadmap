# Question: Wealth equality, finally!
# Categories: 7 Kyu

def redistribute_wealth(wealth: list[int]):
    total_wealth = 0

    for i in range(len(wealth)):
        total_wealth += wealth[i]
    
    distributed_wealth = total_wealth / len(wealth)

    for i in range(len(wealth)):
        wealth[i] = distributed_wealth