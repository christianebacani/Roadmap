# Question: Cat Years, Dog Years (2)
# Categories: 7 Kyu

def owned_cat_and_dog(cat_years, dog_years):
    list_of_cat_years = []
    list_of_dog_years = []

    for i in range(cat_years):
        if i == 0:
            list_of_cat_years.append(15)
        
        elif i == 1:
            list_of_cat_years.append(9)
        
        else:
            list_of_cat_years.append(4)
    
    for i in range(dog_years):
        if i == 0:
            list_of_dog_years.append(15)
        
        elif i == 1:
            list_of_dog_years.append(9)
        
        else:
            list_of_dog_years.append(5)

    human_cat_years = 0
    human_dog_years = 0

    for i in range(len(list_of_cat_years)):
        if cat_years >= list_of_cat_years[i]:
            human_cat_years += 1
            cat_years -= list_of_cat_years[i]
        
        else:
            break
    
    for i in range(len(list_of_dog_years)):
        if dog_years >= list_of_dog_years[i]:
            human_dog_years += 1
            dog_years -= list_of_dog_years[i]
        
        else:
            break
    
    return [human_cat_years, human_dog_years]