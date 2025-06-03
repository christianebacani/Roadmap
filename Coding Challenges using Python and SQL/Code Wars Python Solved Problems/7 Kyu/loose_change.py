# Question: Loose Change!
# Categories: 7 Kyu

def change_count(change: str) -> str:
    CHANGE = {
        'penny': 0.01, 
        'nickel': 0.05, 
        'dime': 0.1, 
        'quarter': 0.25, 
        'dollar': 1.0        
    }
    change = change.split()
    list_of_change = []

    for i in range(len(change)):
        list_of_change.append(CHANGE[change[i]])
    
    return f'${sum(list_of_change):.2f}'